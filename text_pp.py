from pptx import Presentation
import os
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt
import requests
import json
import io
import urllib.parse

dir_path = 'static/presentations'


def parse_response(response):
    slides = response.split('\n\n')
    slides_content = []
    for slide in slides:
        lines = slide.split('\n')
        title_line = lines[0]
        if ': ' in title_line:
            title = title_line.split(': ', 1)[1]  # Extract the title after 'Slide X: '
        else:
            title = title_line
        content_lines = [line for line in lines[1:] if line != 'Content:']  # Skip line if it is 'Content:'
        content = '\n'.join(content_lines)  # Join the lines to form the content
        slides_content.append({'title': title, 'content': content})
    return slides_content


def search_pixabay_images(query):
    API_KEY = os.getenv('PIXABAY_API_KEY')

    # extract keyword
    query = query.split()[-1].lower()
    print(query)
    safe_query = urllib.parse.quote_plus(query)

    PIXABAY_API_URL = f'https://pixabay.com/api/?key={API_KEY}&q={safe_query}&image_type=photo'

    response = requests.get(PIXABAY_API_URL)

    data = json.loads(response.text)

    if 'hits' in data:
        if len(data['hits']) > 0:
            return data['hits'][0]['webformatURL']

    return None


def delete_first_two_slides(presentation):
    slide_ids = [1, 0]
    for slide_id in slide_ids:
        if slide_id < len(presentation.slides):
            xml_slides = presentation.slides._sldIdLst
            slides = list(xml_slides)
            xml_slides.remove(slides[slide_id])


def create_ppt(slides_content, template_choice, presentation_title):
    template_path = os.path.join(dir_path, f"{template_choice}.pptx")

    prs = Presentation(template_path)

    title_slide_layout = prs.slide_layouts[0]
    content_slide_layout = prs.slide_layouts[1]

    # add title slide
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    title.text = presentation_title
    if template_choice == 'dark_modern':
        for paragraph in title.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.name = 'Times New Roman'
                run.font.color.rgb = RGBColor(255, 165, 0)  # RGB for orange color

    # add content slides
    for slide_content in slides_content:
        slide = prs.slides.add_slide(content_slide_layout)

        for placeholder in slide.placeholders:
            if placeholder.placeholder_format.type == 1:  # Title
                placeholder.text = slide_content['title']
                if template_choice == 'dark_modern':
                    for paragraph in placeholder.text_frame.paragraphs:
                        for run in paragraph.runs:
                            run.font.name = 'Times New Roman'
                            run.font.color.rgb = RGBColor(255, 165, 0)  # RGB for orange color
            elif placeholder.placeholder_format.type == 7:  # Content
                placeholder.text = slide_content['content']
                if template_choice == 'dark_modern':
                    for paragraph in placeholder.text_frame.paragraphs:
                        for run in paragraph.runs:
                            run.font.name = 'Times New Roman'
                            run.font.color.rgb = RGBColor(255, 255, 255)  # RGB for white color


        # fetch image URL from Pixabay based on the slide's title
        image_url = search_pixabay_images(slide_content['title'])
        if image_url is not None:
            # download the image
            image_data = requests.get(image_url).content
            # load image into BytesIO object
            image_stream = io.BytesIO(image_data)
            # add the image at the specified position
            slide_width = Inches(20)
            slide_height = Inches(15)

            image_width = Inches(8)  # width of image
            image_height = Inches(5)  # height of image

            left = slide_width - image_width  # calculate left position
            top = slide_height - image_height - Inches(4) # calculate top position

            slide.shapes.add_picture(image_stream, left, top, width=image_width, height=image_height)

    # Delete the first two slides after all new slides have been added
    delete_first_two_slides(prs)

    # Save the presentation
    prs.save(os.path.join('generated', 'generated_presentation.pptx'))

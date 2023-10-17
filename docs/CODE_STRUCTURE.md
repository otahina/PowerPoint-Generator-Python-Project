# Code Structure of the project

## Introduction
This document outlines the structure and functionality of the various modules and functions utilized within this project.

## Utilizing GPT for Presentation Generation

The core functionality of this application is in `flaskapp.py`, where various functions are called to handle different 
aspects of the application. One crucial part of this script is the endpoint defined for generating presentations based 
on user input:

```python
@app.route('/generator', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        number_of_slide = request.form['number_of_slide']
        user_text = request.form['user_text']
        template_choice = request.form.get('template_choice')
        presentation_title = request.form['presentation_title']
        presenter_name = request.form['presenter_name']
        insert_image = 'insert_image' in request.form
```
In the snippet above, we define an endpoint at `/generator` which accepts both `GET` and `POST` requests. 
When a `POST` request is made to this endpoint, the application collects necessary information from the user through 
a form submission. This information includes the number of slides, text content, template choice, presentation title, 
presenter name, and an option to insert images.

The next snippet demonstrates how we prepare the user's input for processing by the GPT model:
```python
user_message = f"I want you to come up with the idea for the PowerPoint. The number of slides is {number_of_slide}. " \
                f"The content is: {user_text}.The title of content for each slide must be unique, " \
                f"and extract the most important keyword within two words for each slide. Summarize the content for each slide. "
```

Rather than passing the raw user_text directly to GPT, we construct a formatted message, user_message, that encapsulates
the user's request in a structured manner. This approach enables a clearer communication of the user's intent to GPT, 
ensuring that the generated presentation aligns with the specified requirements. 
This formatting is robust to variations in user input, accommodating a range of phrasing and request complexities.

For instance, whether a user submits a content request as `Evolution of AI` or phrases it as `Can you make a 
presentation for Evolution of AI with clear examples?`, , the application is designed to interpret and process the 
request effectively.

Keyword extraction is later utilized for retrieving relevant images using the Pexels API.

In the code snippet below, `flaskapp.py` executes three functions:
  - `chat_development()` from `gpt_generate.py` located in `myapp/utils`, to retrieve GPT's response.
  - `parse_response()` from `text_pp.py` located in `myapp/utils`, to process the assistant's response and obtain the 
  - content for the slides.
  - `create_ppt()` from `text_pp.py` located in `myapp/utils`, to forward the slide content, template choice, 
  - presenter's name, and image insertion option.

```python
assistant_response = chat_development(user_message)
# Check the response (for debug)
print(assistant_response)
slides_content = parse_response(assistant_response)
create_ppt(slides_content, template_choice, presentation_title, presenter_name, insert_image)


>print(assistant_response) is used to check if the GPT is correctly responding or not.

```python
assistant_response = chat_development(user_message)
# Check the response (for debug)
print(assistant_response)
slides_content = parse_response(assistant_response)
create_ppt(slides_content, template_choice, presentation_title, presenter_name, insert_image)
```

### `gpt_generate.py`

**build_conversation**

```python
def build_conversation(user_message):
    return [
        {"role": "system",
         "content": "You are an assistant that gives the idea for PowerPoint presentations. When answering, give the user the summarized content for each slide based on the number of slide. "
                    "And the format of the answer must be Slide X(the number of the slide): {title of the content} /n Content: /n content with some bullet points."
                    "Keyword: /n Give the most important keyword(within two words) that represents the slide for each one"},
        {"role": "user", "content": user_message}
    ]
```

This function is defined to accept one argument: user_message, which is made in `flaskapp.py`. 
The content in the "system" role serves as an instruction or a **prompt** for the GPT model, helping to set the context 
or the scenario in which the model should operate. This way, when the model receives the user's request in the "user" 
role, it has a clear understanding of how to handle and respond to that request in a manner that aligns with the given 
instruction. 
In the above code, we include how GPT should answer it in the prompt, so that we can get a response in such a way that,
```
Assistant Response:
Slide 1: Evolution of AI
Content:
- Overview of AI evolution
- Milestones of AI development
- Impact of AI on various industries
- Future prospects of AI
- Ethical considerations in AI development
Keyword: Evolution, AI
```

**generate_assistant_message**

```python
def generate_assistant_message(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response['choices'][0]['message']['content']
```
A request is made to OpenAI's ChatCompletion endpoint using the `openai.ChatCompletion.create` method.
The model parameter specifies the model version to use, in this case, **"gpt-3.5-turbo"**.
The messages parameter passes the conversation array (made in the `chat_development`) to the OpenAI API.
Finally, it extracts and returns the content of the message generated by the assistant.

**chat_development**

```python
conversation = build_conversation(user_message)
    try:
        assistant_message = generate_assistant_message(conversation)
    except openai.error.RateLimitError as e:
        assistant_message = "Rate limit exceeded. Sleeping for a bit..."

    return assistant_message
```

The `try` block attempts to obtain a response from the GPT model by calling the `generate_assistant_message` function
If a `RatelimitError` is encountered (likely due to exceeding the API rate limit), the `except` block is executed. 
In this block, a message "Rate limit exceeded. Sleeping for a bit…" is assigned to `assistant_message`.

If you encounter the "Rate limit exceeded" message, it's advisable to check your OpenAI API usage on
the [OPENAI API Usage](https://platform.openai.com/account/usage) page. This could potentially be a result of exhausting
your API rate limits, and verifying your usage might provide insights into the cause and possible solutions.
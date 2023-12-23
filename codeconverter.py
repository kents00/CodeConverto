import openai

openai.api_key = "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"


def convertlanguage(current_language, target_language, code):
    prompt = f"\"Translate this function from {current_language} into {target_language} full code ### {current_language} \n\n {code} \n\n ### {target_language}"

    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use a different engine based on your needs
        prompt=prompt,
        temperature=0,
        max_tokens=1050,  # Adjust max_tokens as needed
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    # Parse the response to get the response text for our prompt
    generated_text = response['choices'][0]['text']
    return generated_text


this_language = "Python"
intothis_language = "Java"
code = """print("Hello World")"""
print(convertlanguage(current_language=this_language,
      target_language=intothis_language, code=code))

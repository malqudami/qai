from openai import OpenAI

client = OpenAI(api_key= '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')

def get_gpt_response(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    #return response['choices'][0]['message']['content']
    return response.choices[0].message.content.strip()

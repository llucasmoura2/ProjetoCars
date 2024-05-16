from openai import OpenAI
#sk-proj-MMRDOfEtWujP8ISbF6TVT3BlbkFJO3O42j3qhTXv6idF21AY

client = OpenAI(
    api_key='sk-proj-MMRDOfEtWujP8ISbF6TVT3BlbkFJO3O42j3qhTXv6idF21AY'
)


def get_aibio(model, brand, year):
    message = ''''
    me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. fale coisas especeficas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages =[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens = 1000,
        model = 'gpt-3.5-turbo',
    )
    return response.choices[0].message.content
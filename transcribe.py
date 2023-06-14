import openai
import os

# Defina a sua chave de API da OpenAI
openai.api_key = os.environ['API_KEY_GPT']

def translate_text(text):
    # Função para traduzir o texto para o inglês usando a API do ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=1024,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def correct_text(text):
    # Função para corrigir o texto em inglês usando a API do ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=1024,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def process_file(filename):
    # Função para processar o arquivo
    with open(filename, 'r+') as file:
        original_text = file.read()

        # Traduzir palavras entre asteriscos para o inglês
        translated_text = original_text.replace('**', '')
        translated_text = translate_text(translated_text)

        

        # Corrigir o texto traduzido
        corrected_text = correct_text(translated_text)

        # Escrever o texto corrigido abaixo do texto original no mesmo arquivo
        file.write('\n\n--- Texto Corrigido ---\n')
        file.write(corrected_text)

    print('Processamento concluído.')

# Pergunta ao usuário qual o caminho do arquivo a ser processado
file_path = input('Digite o caminho completo do arquivo a ser processado (incluindo a extensão .txt): ')

file_path = os.path.expanduser(file_path)

# Chama a função para processar o arquivo
process_file(file_path)

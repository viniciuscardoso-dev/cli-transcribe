import openai
import os

# Defina a sua chave de API da OpenAI
openai.api_key = os.environ['API_KEY_GPT']

def translate_and_correct_text(text):
    # Função para traduzir e corrigir o texto usando a API do ChatGPT
    response = openai.Completion.create(
        engine='gpt-3.5-turbo-16k-0613',
        prompt=f"Traduza as palavras que estiverem entre asteriscos nesse texto para inglês: {text}\n\nDepois, passe o texto por uma correção ortográfica e me retorne o texto completo corrigido.",
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

        # Traduzir e corrigir o texto
        corrected_text = translate_and_correct_text(original_text)

        # Escrever o texto corrigido abaixo do texto original no mesmo arquivo
        file.write('\n\n--- Texto Corrigido ---\n')
        file.write(corrected_text)

    print('Processamento concluído.')

# Pergunta ao usuário qual o caminho do arquivo a ser processado
file_path = input('Digite o caminho completo do arquivo a ser processado (incluindo a extensão .txt): ')

file_path = os.path.expanduser(file_path)

# Chama a função para processar o arquivo
process_file(file_path)

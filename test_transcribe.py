import os
import pytest
from unittest.mock import AsyncMock
import transcribe

@pytest.mark.asyncio
async def test_process_file():
    file_path = '~/PROJETOS/cli-transcribe/texto_example.txt'

    file_path = os.path.expanduser(file_path)

    # Mock das chamadas à API e da função process_file
    with AsyncMock() as mock_translate_text, \
         AsyncMock() as mock_correct_text, \
         AsyncMock() as mock_process_file:

        # Configuração dos retornos mockados
        mock_translate_text.return_value.__aenter__.return_value.choices[0].text.strip.return_value = 'Texto traduzido'
        mock_correct_text.return_value.__aenter__.return_value.choices[0].text.strip.return_value = 'Texto corrigido'

        # Execução da função process_file
        await transcribe.process_file(file_path)

        # Verificações
        mock_translate_text.assert_called_once_with('Texto a ser traduzido')
        mock_correct_text.assert_called_once_with('Texto traduzido')
        mock_process_file.assert_called_once_with(file_path)

if __name__ == '__main__':
    pytest.main()

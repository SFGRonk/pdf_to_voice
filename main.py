from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path

def pdf_to_voice(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        with open('text.txt', 'w') as file:
            file.write(text)

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!\n---Hanve a nice day!---'

    else: 
        return 'File is not exist!'
    
def main():
    tprint('PDF ___ TO ___ VOICE')
    file_path = input("\nEnter a file's path: ")
    language = input("\nEnter language, for example 'en' or 'ru': ")
    print(pdf_to_voice(file_path=file_path, language=language))

if __name__ == '__main__':
    main()
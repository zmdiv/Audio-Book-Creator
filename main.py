from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path

# checking if the file to work with exists
def pdf_to_mp3(file_path= 'test.pdf', language= 'en'): 
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        return 'File exists'
    
# extracting text from every page of the pdf file and cleaning it
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')

# creating .mp3 file from the text. indicating language and pace. 
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'{file_name}.mp3 saved succesfully'
    else:
        return 'File does not exist, please check again'
    
#  accepting inputs and calling above created function in the main functions. 
def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input('enter the file path: ')
    language = input('enter the language acronyme, for example "en" or "es" ')
    return pdf_to_mp3(file_path=file_path, language=language)

if __name__ == '__main__':
    main()


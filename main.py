import PyPDF2
import pyttsx3
import signal
import sys
from common.utils import Utils

utils = Utils()
language = 'spanish-latin-am'
engine = pyttsx3.init()
project_path = utils.get_project_path()
project_path = utils.parse_path(f'{project_path}/')
open_book = open(f'{project_path}test1.pdf', 'rb')


def get_voice_position() -> str:
    voices = engine.getProperty('voices')
    i: int = 0

    for voice in voices:
        if voice.id == language:
            return voices[i].id
        else:
            i = i + 1


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C')

    try:
        pdfReader = PyPDF2.PdfFileReader(open_book)
        pdf_text = ''

        for page in pdfReader.pages:
            text = page.extractText().replace('\n', '')
            if text != '':
                engine.setProperty('voice', get_voice_position())
                engine.say(text)
                engine.runAndWait()
    except KeyboardInterrupt:
        engine.stop()
        signal.shutdown()
        print('Close program')
    except Exception as e:
        print(e)
    finally:
        open_book.close()

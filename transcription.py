from sys import argv
import os

# setting-up directory location #
global directory
directory = argv[1]

global DIR_REL_PATH
DIR_REL_PATH = f"../{directory}"
#################################

def get_abs_path():
    pass

def write_output():
    files = sorted(os.listdir(f"{DIR_REL_PATH}"), key=lambda x: x.split(".")[0])
    is_h1_setted = False
    for file in files:
        name, _ = file.split(".")
        call_whisper(file)
        with open(f"{DIR_REL_PATH}/output/{name}.txt") as text:
            with open(f"{DIR_REL_PATH}/transcricao.md", "a") as audio_markdown:
                if not is_h1_setted:
                    audio_markdown.write(f"# Transcrições dos audios de {directory}")
                    is_h1_setted = True

                audio_markdown.write(f"## {directory} audio {name}\n\n{text.read()}\n")

def call_whisper(file):
    command_line = f"whisper --model tiny {DIR_REL_PATH}/{file} --language pt -f txt --verbose False -o {DIR_REL_PATH}/output"
    os.system(command_line)

if __name__ == "__main__":
    write_output()

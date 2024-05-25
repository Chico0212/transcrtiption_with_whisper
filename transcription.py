#!/usr/bin/python3
# caso esteja usando, opte pelo interpretador da pyvenv

from sys import argv
import os

def get_abs_path(dir: str) -> tuple[str]:
    if dir[0] == "/" or dir[:2] == "./" or dir[:3] == "../":
        return dir, dir.split("/")[-1]
    return f"./{dir}", dir.split("/")[-1]

def write_output(audio_dir_path, audio_dir_name):
    try:
        files = sorted(os.listdir(f"{audio_dir_path}"), key=lambda x: x.split(".")[0])
    except:
        print(f"DIRETÓRIO: {audio_dir_name} NÃO ENCONTRADO")
        return

    is_h1_setted = False
    for file in files:
        name = file.split(".")[0]
        call_whisper(file, audio_dir_path)
        with open(f"{audio_dir_path}/output/{name}.txt") as text:
            with open(f"{audio_dir_path}/transcricao.md", "a") as audio_markdown:
                if not is_h1_setted:
                    audio_markdown.write(f"# Transcrições dos audios de {audio_dir_name}\n\n")
                    is_h1_setted = True

                audio_markdown.write(f"## {audio_dir_name} audio {name}\n\n{text.read()}\n")

def call_whisper(file, audio_dir_path):
    command_line = f"whisper --model tiny {audio_dir_path}/{file} --language pt -f txt --verbose False -o {audio_dir_path}/output"
    os.system(command_line)

if __name__ == "__main__":
    directories = argv[1:]
    for directory in directories:
        write_output(*get_abs_path(directory))

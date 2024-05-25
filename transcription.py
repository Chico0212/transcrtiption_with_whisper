#!/usr/bin/python3
# caso esteja usando, opte pelo interpretador da pyvenv

from sys import argv
import os
import whisper

def path_treatment(dir: str) -> tuple[str]:
    if "/" not in dir and "\\" not in dir:
        raise BaseException(f"""[ERRO] PATH "{dir}" INVÁLIDO""")
    return dir, dir.split("/")[-1]

def write_files(files, audio_dir_path, audio_dir_name):
    is_h1_setted = False
    for file in files:
        name = file.split(".")[0]
        call_whisper(file, audio_dir_path)
        with open(f"{audio_dir_path}/output/{name}.txt") as text, open(f"{audio_dir_path}/transcricao.md", "a") as audio_markdown:
            if not is_h1_setted:
                audio_markdown.write(f"# Transcrições dos audios de {audio_dir_name}\n\n")
                is_h1_setted = True

            audio_markdown.write(f"## {audio_dir_name} audio {name}\n\n{text.read()}\n")

def start_transcription(audio_dir_path, audio_dir_name):
    try:
        files = sorted(os.listdir(f"{audio_dir_path}"), key=lambda x: x.split(".")[0])
    except :
        print(f"[ALERTA] DIRETÓRIO: {audio_dir_name} NÃO ENCONTRADO")
        return

    write_files(files, audio_dir_path, audio_dir_name)

def call_whisper(file, audio_dir_path):
    # return whisper.load_model("tiny")\
    #     .transcribe(
    #         audio=f"{audio_dir_path}/{file}", 
    #         decode_options={"language": "pt"}, 
    #         verbose=False,
    #         )
    
    command_line = f"whisper --model tiny {audio_dir_path}/{file} --language pt -f txt --verbose False -o {audio_dir_path}/output"
    os.system(command_line)

if __name__ == "__main__":
    directories = argv[1:]
    for directory in directories:
        start_transcription(*path_treatment(directory))

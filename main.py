import yt_dlp
import os

def download_youtube_videos(pairs, output_path):
    # Cria a pasta caso ela não exista
    os.makedirs(output_path, exist_ok=True)
    
    # Configurações do yt-dlp
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Define o caminho de saída com título do vídeo
    }
    
    # Baixa cada par de vídeos
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for pair in pairs:
            urls = pair.split(',')
            for url in urls:
                try:
                    print(f"Baixando: {url.strip()}")
                    ydl.download([url.strip()])
                except Exception as e:
                    print(f"Erro ao baixar {url.strip()}: {e}")

if __name__ == "__main__":
    # Pergunta ao usuário qual caminho de saída usar
    choice = input("Escolha o caminho de saída (0 para ./videosEditar/ ou 1 para ./videoVicios/): ").strip()

    if choice == '0':
        output_path = './videosEditar/'
    elif choice == '1':
        output_path = './videoVicios/'
    else:
        print("Escolha inválida. Usando o caminho padrão ./videosEditar/")
        output_path = './videosEditar/'

    # Caminho do arquivo de texto com as URLs (no mesmo diretório que main.py)
    file_path = 'urlsvideos.txt'
    
    # Lê o arquivo de texto e extrai os pares de URLs
    with open(file_path, 'r') as file:
        video_pairs = [line.strip() for line in file.readlines()]
    
    # Chama a função para baixar os vídeos
    download_youtube_videos(video_pairs, output_path)

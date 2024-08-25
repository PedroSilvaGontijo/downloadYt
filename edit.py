import moviepy.editor as mp
import os

def merge_videos(main_video_path, secondary_video_path, output_path):
    # Carregar os vídeos
    main_video = mp.VideoFileClip(main_video_path)
    secondary_video = mp.VideoFileClip(secondary_video_path)

    # Dimensões dos vídeos
    width, height = main_video.size

    # Redimensionar os vídeos para garantir que ocupem metade da tela
    main_video_resized = main_video.resize(height=height // 2)
    secondary_video_resized = secondary_video.resize(height=height // 2)

    # Criar um vídeo em loop para o vídeo secundário até o comprimento do vídeo principal
    secondary_video_looped = secondary_video_resized.loop(duration=main_video_resized.duration)

    # Dividir a tela em duas partes: superior para o vídeo principal e inferior para o vídeo secundário
    final_video = mp.clips_array([
        [main_video_resized],
        [secondary_video_looped]
    ])

    # Especificar que o áudio será do vídeo principal
    final_video = final_video.set_audio(main_video_resized.audio)

    # Salvar o vídeo final
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

def process_videos(main_video_dir, secondary_video_dir, output_video_path):
    # Listar todos os arquivos de vídeo nos diretórios
    main_videos = sorted([f for f in os.listdir(main_video_dir) if f.endswith(('.mp4', '.mkv', '.webm'))])
    secondary_videos = sorted([f for f in os.listdir(secondary_video_dir) if f.endswith(('.mp4', '.mkv', '.webm'))])

    # Processar os pares de vídeos
    for i in range(min(len(main_videos), len(secondary_videos))):
        main_video_path = os.path.join(main_video_dir, main_videos[i])
        secondary_video_path = os.path.join(secondary_video_dir, secondary_videos[i])
        output_path = os.path.join(output_video_path, f"merged_output_{i + 1}.mp4")
        print(f"Processando: {main_video_path} + {secondary_video_path} -> {output_path}")
        merge_videos(main_video_path, secondary_video_path, output_path)

if __name__ == "__main__":
    main_video_directory = './videosEditar/'
    secondary_video_directory = './videoVicios/'
    output_video_path = os.path.expanduser('~/Área de Trabalho/TiktokUploader/TiktokAutoUploader/VideosDirPath')
    process_videos(main_video_directory, secondary_video_directory, output_video_path )

from pytube import YouTube

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_quality()
    try:
        youtubeObject.download()
    except:
        print('Aconteceu um erro ao baixar o vídeo!')
    print('Vídeo baixado com sucesso!')

link = input('Insira o link para download aqui! URL: ')
download(link)

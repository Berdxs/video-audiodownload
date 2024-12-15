from yt_dlp import YoutubeDL
import yt_dlp 





op = input("\n[1] para baixar videos [2] para baixar audio dos videos! ")

url = input("Digite a URL do vídeo do YouTube: ")

match op:

    case '1':

        try:
            output_directory ='C:/Users/capan/Desktop/minha pasta/%(title)s.%(ext)s'

            ydl_opts = {
                'format': 'best',  
                'outtmpl': output_directory,  
            }


            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])  

            print("Download concluído!")

        except Exception as e:
        
            print(f"Erro ao tentar baixar o vídeo: {e}")
    case '2':
        try:
            output_directory ='C:/Users/capan/Desktop/minha pasta/%(title)s.%(ext)s'
            op = {
                'format': 'bestaudio/best',
                'outtmpl': output_directory,
                'noplaylist': True,
                'extractaudio': True,
                'audioquality': 1
                
                            
            }
           

            with YoutubeDL(op) as ydl:
           
                ydl.download([url])
            

        except Exception as e:
        
            print(f"Erro ao tentar baixar o vídeo: {e}")
    


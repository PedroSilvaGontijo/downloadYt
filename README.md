Esse é um programa para baixar vídeos do youtube/youtube shorts.
Para instalar no seu computador utilize o comando "git clone https://github.com/PedroSilvaGontijo/downloadYt.git" e instale as dependências.
Preencha as urls dos vídeos no arquivo urlsvideos.txt e digite o comando "python3 main.py" e escolha o diretório em que o vídeo será salvo, (0 para vídeos principais e 1 para vídeos viciantes)
Caso queira editar os vídeos para juntar vídeos dos dois diretórios rode o comando "python3 edit.py". *Importante* Modifique o path do ditório final nesse arquivo.
O arquivo edit.py editará os vídeos salvos nos dois diretórios e juntará os vídeos em ./videosEditar e ./videosEditar onde vídeos na primeira página será o vídeo principal, ficará em cima e terá o aúdio, enquanto os vídeos em ./videosEditar ficará embaixo sem som.

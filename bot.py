import requests, base64, json, shutil, openai, time, datetime, urllib.request, urllib.error, os.path, re
from bs4 import BeautifulSoup
#import sheets  # Importe o módulo sheets.py
from io import BytesIO
from requests.exceptions import Timeout


titulo_anterior_path = "titulo_anterior.txt"
def ler_titulo_anterior():
    if os.path.exists(titulo_anterior_path):
        with open(titulo_anterior_path, 'r') as file:
            return file.read().strip()
    else:
        return ""
def salvar_titulo_anterior(titulo):
    with open(titulo_anterior_path, 'w') as file:
        file.write(titulo)

titulo_anterior = ler_titulo_anterior()




# Defina um limite de tempo limite personalizado (em segundos)
timeout = 10

try:
    # Faz uma solicitação HTTP com um objeto timeout personalizado
    response = urllib.request.urlopen('https://noiteassombrada.serv00.net/wp-json/wp/v2/posts', timeout=timeout)

    # Print the response from the REST API
    print(response)

except urllib.error.URLError as e:
    print(f'Request error: {e}')




while True:
    try:
        # Faz uma solicitação HTTP com um objeto timeout personalizado
        response = urllib.request.urlopen('https://noiteassombrada.serv00.net/wp-json/wp/v2/posts', timeout=timeout)
        print(response)
    except Timeout:
        print('Erro de timeout. Tentando novamente...')
    except urllib.error.URLError as e:
        print(f'Request error: {e}')
    # Obter a hora atual
    now = datetime.datetime.now()

    # Formatar a hora no formato solicitado
    formatted_time = now.strftime("%Y-%m-%dT%H:%M:%S")

    # Imprimir a hora
    print(formatted_time)

    # Aguardar 1 segundo antes de imprimir a hora novamente
    time.sleep(1)
    response = requests.get('https://ovnihoje.com/') #SITE COMPLETO
    content = response.content #DIZER O QUE INTERESSA NA PÁGINA = CONTEÚDO
    site = BeautifulSoup(content,'html.parser') #CONVERSÃO DO CONTEÚDO PARA HTML
    novidade = site.find('div', attrs={'class': 'item-inner'}) #OBTER CONTEÚDO DO DIV "INTER-INNER"(NO CASO, DAS NOVIDADES)
    titulo_noticia = novidade.find('h2', attrs={'class': 'title'}) #EXTRAIR TÍTULO DA NOTÍCIA = titulo_noticia.text
    hora_noticia = novidade.find('span', attrs={'class': 'time'}) #EXTRAIR HORÁRIO DA NOTÍCIA = horario_noticia.text
    noticia_titulo = novidade.find('h2', attrs={'class': 'title'}) #EXTRAIR TÍTULO DA NOTÍCIA = noticia_titulo.text
    noticia_hora = novidade.find('span', attrs={'class': 'time'}) #EXTRAIR HORÁRIO DA NOTÍCIA = noticia_hora.text
    noticia_imagem = novidade.find('a', attrs={'class': 'img-holder'}) #EXTRAIR LINK DA IMAGEM DA NOTICIA = noticia_imagem['data-bsrjs']
    noticia_link = imagem_noticia = novidade.find('a', attrs={'class': 'img-holder'}) #EXTRAIR LINK DA IMAGEM DA NOTICIA = noticia_link['href']
    noticia_conteudo = noticia_link['href']
    response2 = requests.get(noticia_conteudo) #SITE DO CONTEUDO DA NOTICIA
    content2 = response2.content 
    conteudo = BeautifulSoup(content2,'html.parser') #CONVERSÃO DO CONTEÚDO PARA HTML
    descricao_conteudo = conteudo.find('div', attrs={'class': 'single-container'})
    introducao_conteudo = descricao_conteudo.find('p', attrs={'class': 'bs-intro'}) #EXTRAIR SUBTÍTULO DA NOTÍCIA = introducao_conteudo.text
    conteudo_texto = descricao_conteudo.find('div', attrs={'class': 'entry-content clearfix single-post-content'}) #EXTRAIR TEXTO DA NOTÍCIA = conteudo_texto.text (AINDA PRECISA REMOVER PARTES INSIGNIFICANTES)





    texto = conteudo_texto.text





    frase_anterior = " min." #excluir tudo que vem antes de "tempo de leitura x min."
    partes = texto.split(frase_anterior)
    if len(partes) > 1:
        texto_anterior = partes[1]
    else:
        texto_anterior = texto
        
    formatacao = texto_anterior
    frase_posterior = "(Fonte"
    partes = formatacao.split(frase_posterior)
    texto_final = partes[0]







    #print(texto_final)
    titulo = titulo_noticia.text
    subtitulo = introducao_conteudo.text
    horario = noticia_hora.text
    






    def extrair_url_imagem(html_string):
        """
        Extrai o URL da imagem de um trecho de HTML.

        Parâmetros:
        - html_string (str): Trecho de HTML contendo a tag <a> com a classe 'img-holder'.

        Retorna:
        - str: URL da imagem encontrada no atributo 'style' da tag <a>.
        """
        # Usando BeautifulSoup para analisar o trecho de HTML
        soup = BeautifulSoup(html_string, 'html.parser')

        # Procurando pela tag <a> com a classe 'img-holder'
        img_tag = soup.find('a', class_='img-holder')

        # Verificando se a tag foi encontrada
        if img_tag:
            # Extraindo o valor do atributo 'style'
            style_value = img_tag.get('style')
            
            # Usando uma expressão regular para encontrar o URL da imagem dentro do valor do atributo 'style'
            img_url_match = re.search(r'url\((.*?)\)', style_value)
            
            if img_url_match:
                # Extraindo o URL da imagem
                img_url = img_url_match.group(1)
                return img_url
            else:
                return 'URL da imagem não encontrada.'
        else:
            return 'Tag <a> com a classe "img-holder" não encontrada.'

    # Exemplo de uso da função
    # Primeiro, precisamos converter o objeto BeautifulSoup para uma string de HTML
    html_string = str(noticia_link)
    url_imagem = extrair_url_imagem(html_string)
    print(url_imagem)





    imagem_noticia = url_imagem


    print(imagem_noticia)

    if titulo != titulo_anterior:
        # Faz o download da imagem
        print("Nova notícia encontrada:", titulo)
        try:
            response = requests.get(imagem_noticia)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f'Error during download: {err}')
            exit()

        # Armazena a imagem em uma variável
        imagem = BytesIO(response.content)

        # Nome do arquivo de saída
        saida = 'media/image.jpg'

        # Cria o diretório se ele não existir
        os.makedirs(os.path.dirname(saida), exist_ok=True)

        # Salva a imagem no disco
        try:
            with open(saida, 'wb') as f:
                shutil.copyfileobj(imagem, f)
        except IOError as err:
            print(f'Error during save: {err}')
            exit()

        print(f'Imagem salva em {saida}')


        #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||REDATOR!||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

        def ask_question(question):
            openai.api_key = "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"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=[{"role": "user", "content": question}],
                max_tokens=1500,
                n=1,
                stop=None,
                temperature=0.5,
            )
            return response.choices[0].message.content.strip()

        question = f"Quero que você faça 3 coisas com esse texto. 1° Reescreva ele usando uma linguagem de texto mais empolgante. 2° remova qualquer mensão ao 'OVNI Hoje'. 3° Finalize o texto incentivando as pessoas a seguir nossa página no facebook: 'https://www.facebook.com/investigadoresufologico'(transforme isso em um link clicável) Aqui está o texto:  {texto_final}   "
        response = ask_question(question)

        #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        





        # Set up the WordPress site details and authentication
        url = "https://noiteassombrada.serv00.net/wp-json/wp/v2"
        user = 'noiteassombrada'
        password = "RFae zZcT QITl 9bgK Io8g JbJf"

        creds = user + ':' + password

        token = base64.b64encode(creds.encode()).decode('utf-8')

        header = {'Authorization': 'Basic ' + token}

        # Carregar a imagem
        media = {
            'file': open('media/image.jpg', 'rb'),
            'caption': titulo,
            'description': titulo
        }

        image = requests.post(url + '/media', headers=header, files=media)
        imageURL = str(json.loads(image.content)['source_url'])

        # Salvar o ID da mídia
        image_id = json.loads(image.content)['id']

        # Criar o post
        post = {
            "date": formatted_time,
            "title": titulo,
            "slug": "Este é o Slug",
            "status": "publish",
            "content": response, 
            "author": "1",
            "format": "standard",
            "featured_media": image_id
        }


        # Carregar as categorias#############################################################
        categorias = ['Relatos', 'Artigo', 'Noticias']
        # Obter os IDs das categorias
        categoria_ids = []
        for categoria in categorias:
            response = requests.get(url + "/categories?search=" + categoria, headers=header)
            if response.status_code == 200:
                categoria_id = json.loads(response.content)[0]['id']
                categoria_ids.append(categoria_id)
            else:
                print("Erro ao obter a categoria:", response.status_code)
        # Adicionar a categoria ao post
        categoria_ids = []
        response = requests.get(url + "/categories?search=Noticias", headers=header)
        if response.status_code == 200:
            categoria_id = json.loads(response.content)[0]['id']
            categoria_ids.append(categoria_id)
        else:
            print("Erro ao obter a categoria:", response.status_code)

        post['categories'] = categoria_ids
        #################################################################################

     

        tags = [titulo, "UAPs," "Fenômenos Aéreos Não Identificados", "Vida extraterrestre", "Inteligência extraterrestre", "Objetos voadores não identificados", "Ovnis", "Discos voadores", "Contato extraterrestre", "Abdução alienígena", "Área 51", "Roswell", "Fenômenos paranormais"]

        # Obter os IDs das tags
        tag_ids = []
        for tag in tags:
            response = requests.get(url + "/tags?search=" + tag, headers=header)
            if json.loads(response.content):
                tag_id = json.loads(response.content)[0]['id']
                tag_ids.append(tag_id)
            else:
                # Tentar criar a tag se ela não existir
                response = requests.post(url + "/tags", headers=header, json={'name': tag})
                if response.status_code == 201:
                    tag_id = json.loads(response.content)['id']
                    tag_ids.append(tag_id)
                else:
                    print("Erro ao criar a tag:", response.status_code)

        # Adicionar a tag ao post
        post['tags'] = tag_ids


        # Enviar o post
        response = requests.post(url + "/posts", headers=header, json=post)

        # Print the response from the REST API
        print(response)
        salvar_titulo_anterior(titulo)
        titulo_anterior = titulo
        time.sleep(21600)
    else:
        print("Não tem postagens novas...")
        time.sleep(21600 )



























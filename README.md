# Noite Assombrada

Este é o repositório do projeto "Noite Assombrada", onde você encontrará o código-fonte de um bot criado para interagir com informações sobre o site [Noite Assombrada](https://noiteassombrada.serv00.net/) e publicar notícias em um site WordPress.

## Sobre o Projeto

O objetivo deste projeto é automatizar a busca por novidades no site "Noite Assombrada" e publicá-las em um site WordPress. O bot busca por informações relevantes no site principal, extrai o conteúdo das notícias, realiza um processamento de linguagem natural para reescrever o texto de forma mais empolgante, e então publica a notícia no WordPress.

## Funcionalidades

- **Coleta de Dados:** O bot faz solicitações HTTP ao endpoint do site "Noite Assombrada" para obter informações sobre as últimas notícias.
- **Extração de Conteúdo:** As notícias são extraídas do site principal, incluindo título, subtítulo, horário, conteúdo e imagem.
- **Processamento de Texto:** O conteúdo das notícias é processado usando inteligencia artificial para reescrever o texto de forma mais empolgante e remove menções ao site.
- **Publicação Automática:** As notícias são publicadas automaticamente em um site WordPress.
- **Agendamento:** O bot é executado periodicamente para verificar novas notícias a cada seis horas.

## Configuração

Para executar o código deste projeto, siga estas etapas:

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter todas as dependências instaladas, você pode instalá-las usando pip:

    ```bash
    pip install requests beautifulsoup4 openai
    ```

3. Configure as variáveis de ambiente para o WordPress (URL do site, nome de usuário, senha).
4. Execute o script `bot.py`.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este projeto, siga estas etapas:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/FeatureIncrivel`).
3. Faça commit de suas alterações (`git commit -am 'Adicione uma feature incrível'`).
4. Faça push para a branch (`git push origin feature/FeatureIncrivel`).
5. Abra um pull request.

## Contato

Você pode me contatar diretamente por [e-mail](mailto:seuemail@exemplo.com) ou através do meu perfil do [GitHub](https://github.com/seuusuario). 

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT) - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.

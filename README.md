# PUC-RIO: especialização em Engenharia de Software
## Sprint 3
## Componente 2: cadastro de eventos

### Descrição

Este componente, ao receber dados de eventos provenientes do componente 1 (https://github.com/anttoniol/pucrio_engsoft_sprint3_comp1_2024), 
cadastra eventos e as coordenadas da localização de cada evento.

### Instruções de uso

#### API: Inicialização
1. Clonar o repositório
2. Pelo terminal, acessar a pasta do repositório
3. Criar uma cópia do arquivo "model.properties.ini"
4. Renomear a cópia para "properties.ini"

#### API: Execução
##### Com Docker Compose
1. Na pasta do componente, executar o Dockerfile usando o comando `sudo docker-compose up` ou `sudo docker compose up`
2. Acessar o endereço http://localhost:5000/swagger , para utilizar os endpoints

##### Sem Dockerfile
1. Na pasta do componente, criar um ambiente virtual, conforme explicado em https://www.alura.com.br/artigos/ambientes-virtuais-em-python?gclid=Cj0KCQjw6cKiBhD5ARIsAKXUdyaJkqNkWzEWgYdNgrCXhupl1irAxb_tmcN0RmpRj1htFv8RsRSQ9KwaAvmqEALw_wcB
2. Executar o comando pip install -r requirements.txt, para instalar as bibliotecas necessárias
3. Substituir o valor "db" do parâmetro "host" por "localhost", no arquivo api/repositories/repository.py
4. MySQL:
   1. Instalar o software (no Ubuntu, as instruções estão em https://ubuntu.com/server/docs/install-and-configure-a-mysql-server)
   2. Dentro do MySQL, executar o script SQL contido no diretório "db" do projeto
6. No diretório "api", rodar a aplicação: python3 controller.py
5. Acessar o link http://localhost:5000/swagger, para fazer alguma requisição à API


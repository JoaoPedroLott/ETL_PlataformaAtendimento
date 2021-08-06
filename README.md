<h1 align="center">Case: Plataforma de atendimento</h1>
<p align="center">Este projeto consiste na resolução do desafio proposto pela EloGroup</p>

## Tabela de conteúdos
* [Tasks](#Tasks)
* [Arquitetura](#Arquitetura)
* [Modelo de dados](#Modelo de dados)
* [ETL](#ETL)
* [Testes](#Testes)

## Tasks
* Construir uma sugestão de arquitetura tecnológica consistente para resolver o problema apresentado,
inclusive com sugestão de ferramentas, serviços em nuvem, integrações etc.

* Desenvolver uma proposta de modelo de dados para armazenar as informações que respondem às
necessidades de informação relatadas.

* Construir um ETL que capture dados de um tópico do Apache MQ e que sirva para alimentar todo ou parte do
modelo de dados proposto.

## Arquitetura
* Utilizar um ETL desenvolvido em python para consumir os dados do Apache MQ utilizando o protocolo stomp (por conta da facilidade de integração)
* Salvar os dados obtidos pelo consumo do tópico em um banco de dados NoSQL Mongo DB localizado em um fornecedor de cloud (Amazon, Azure, Google, etc)
  seguindo o modelo de dados proposto para o arquivo Json. (Optei pelo Mongo DB pois é uma boa opção para armazenar grandes volumes de dados
  e por trabalhar com arquivos Json, o mesmo formato do modelo de dados proposto, facilitando assim a integração)
	
## Modelo de dados
O modelo de dados proposto segue a seguinte estrutura em Json:
```javascript
{
     'name': 'Geralt',
     'document': '123.456.789-12',
     'age': '40',
     'sex': 'masculino',
     'channel': 'whatsapp',
     'services': {
                    '1': 'agendar consulta',
                    '2': 'informacoes'
                  },
     'date': '02/08/2021 11:35:42',
     'headache': 'sim',
     'otherSymptoms': 'nao',
     'covidContact': 'nao',
     'covidTest': 'negativo',
     'serviceScore': '10',
     'solved': 'sim'
}
```

## ETL
O ETL proposto foi desenvolvido e pode ser executado pelo arquivo principal Main.py localizado
na pasta main na raiz do projeto.

## Testes
Para a execução do projeto é necessário subir o container em docker contendo o Mongo DB e o 
Mongo Express, localizados no arquivo docker-compose.yml.


Para o ETL ser executado com sucesso foi desenvolvida uma função de producer, onde alguns dados
são gerados, no formato de dados proposto, para que estes possam ser consumidos pelo ETL e salvos no
Mongo DB. 

Os arquivos com os scripts de teste podem ser localizados na pasta teste na raiz do projeto.
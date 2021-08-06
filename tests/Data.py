import json

Json1 = {'name': 'Geralt',
         'document': '123.456.789-12',
         'age': '40',
         'sex': 'masculino',
         'channel': 'whatsapp',
         'services': {'1': 'agendar consulta',
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
Json1 = json.dumps(Json1)

Json2 = {'name': 'Yennifer',
         'document': '987.654.321-00',
         'age': '35',
         'sex': 'feminino',
         'channel': 'telegram',
         'services': {'1': 'informacoes',
                      '2': 'agendar consulta',
                      '3': 'cancelar consulta'
                      },
         'date': '03/08/2021 17:41:20',
         'headache': 'nao',
         'otherSymptoms': 'nao',
         'covidContact': 'nao',
         'covidTest': 'negativo',
         'serviceScore': '6',
         'solved': 'nao'
         }
Json2 = json.dumps(Json2)

Json3 = {'name': 'Dandelion',
         'document': '987.123.654-99',
         'age': '29',
         'sex': 'masculino',
         'channel': 'telefone',
         'services': {'1': 'solicitar atendimento'
                      },
         'date': '05/08/2021 15:02:50',
         'headache': 'sim',
         'otherSymptoms': 'nao',
         'covidContact': 'sim',
         'covidTest': 'postivio',
         'serviceScore': '8',
         'solved': 'nao'
         }
Json3 = json.dumps(Json3)

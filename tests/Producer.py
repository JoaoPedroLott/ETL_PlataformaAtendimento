from tests import Data
import time


def sender(conexao):
    x = 0
    while x < 5:
        conexao.send(body=Data.Json1, destination='processo-elo')
        time.sleep(3)
        conexao.send(body=Data.Json1, destination='processo-elo')
        time.sleep(3)
        conexao.send(body=Data.Json2, destination='processo-elo')
        time.sleep(3)
        conexao.send(body=Data.Json2, destination='processo-elo')
        time.sleep(3)
        conexao.send(body=Data.Json2, destination='processo-elo')
        time.sleep(3)
        conexao.send(body=Data.Json3, destination='processo-elo')
        time.sleep(3)
        conexao.send(body=Data.Json3, destination='processo-elo')
        time.sleep(3)
        conexao.send(body=Data.Json3, destination='processo-elo')
        time.sleep(3)
        conexao.send(body=Data.Json3, destination='processo-elo')
        time.sleep(3)
        x += 1

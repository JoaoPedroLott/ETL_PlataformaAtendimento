import stomp
import json
import DataLoad


class ListenerMQ(stomp.ConnectionListener):
    def on_error(headers, message):
        print("Received an error ", message)

    def on_message(headers, message):
        messageHeader = message.headers
        body = message.body
        bodyJson = json.loads(body)

        resp = {"Header": messageHeader, "Body": bodyJson}
        # print(resp)

        # Insert into mongo
        DataLoad.insert(resp)
        print('Mensagem recebida.')

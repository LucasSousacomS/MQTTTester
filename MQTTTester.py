import time
from paho.mqtt import client as mqtt_client

broker = 'broker.hivemq.com'
port = 1883
topic = "smart/mqtt"
client_id = 'testemqtt'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, selecao):
    if selecao == 1:
        client.publish(topic,"a",0)
    if selecao == 2:
        client.publish(topic,"b",0)
    if selecao == 3:
        client.publish(topic,"c",0)
    if selecao == 4:
        client.publish(topic,"d",0)
    if selecao == 5:
        client.publish(topic,"e",0)

def main():
    client = connect_mqtt()
    while True:
        print(f"1 - a \n2 - b\n3 - c\n4 - d\n5 - e")
        selecao = int(input("Selecione o que deseja fazer: "))
        client.loop_start()
        time.sleep(1)
        publish(client, selecao)
        client.loop_stop()
        time.sleep(1)

if __name__ == '__main__':
    main()

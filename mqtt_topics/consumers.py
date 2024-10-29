import json

from mqttasgi.consumers import MqttConsumer

class GrandeurMqttConsumer(MqttConsumer):

    async def connect(self):
        await self.subscribe('sensor/temperature', 2)
        print('MQTT connected....')
    
    async def receive(self, mqtt_message):
        print(f'Received message topic: {mqtt_message['topic']}')
        print(f'with payload {mqtt_message['payload']}')
        print(f'And QoS {mqtt_message['qos']}')
    
    async def disconnect(self):
        await self.unsubscribe('sensor/temperature')




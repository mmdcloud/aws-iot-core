#!/usr/bin/env python3
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
import time

# Configuration
ENDPOINT = "${data.aws_iot_endpoint.current.endpoint_address}"
CLIENT_ID = aws_iot_thing.iot_device.name
PATH_TO_CERT = "/etc/aws-iot/device-cert.pem"
PATH_TO_KEY = "/etc/aws-iot/private-key.pem"
PATH_TO_ROOT = "/etc/aws-iot/AmazonRootCA1.pem"

# Spin up resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=PATH_TO_CERT,
    pri_key_filepath=PATH_TO_KEY,
    client_bootstrap=client_bootstrap,
    ca_filepath=PATH_TO_ROOT,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=6
)

# Connect
connect_future = mqtt_connection.connect()
connect_future.result()
print("Connected!")

# Publish a message
mqtt_connection.publish(
    topic="iot/ec2",
    payload="Hello from EC2 IoT Device",
    qos=mqtt.QoS.AT_LEAST_ONCE
)

# Disconnect
time.sleep(5)
disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()
# alarm_gateway
Alarm gateway for Home Assistant: Make call and send sms to the phone number

1- Setup 
1.1- Create a directory custom_components in your Home Assistant configuration directory.

1.2- Copy ```alarm_gateway``` from this project including all files into the directory custom_components.
.homeassistant/
|-- custom_components/
|   |-- alarm_gateway/
|       |-- __init__.py
|       |-- alarm_gateway.so
|       |-- manifest.json
|       |-- services.yaml

1.3. Add the following to your configuration.yaml file.
```alarm_gateway:```


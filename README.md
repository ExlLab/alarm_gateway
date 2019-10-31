# alarm_gateway
Alarm gateway for Home Assistant: Make call and send sms to the phone number

1- Setup

1.1- Create a directory custom_components in your Home Assistant configuration directory.

1.2- Copy ```alarm_gateway``` from this project including all files into the directory ```custom_components```.
.homeassistant/

|-- custom_components/
|   |-- alarm_gateway/
|       |-- __init__.py
|       |-- alarm_gateway.so
|       |-- manifest.json
|       |-- services.yaml

1.3- Add the following to your configuration.yaml file.
```alarm_gateway:```

Check config anh restart Home Assistant.

2. Add entities for component ```alarm_gateway```

```
# input_text.yaml
alarm_phones_call:
  name: 'Số điện thoại gọi'
  icon: mdi:contact-phone 
  
alarm_phones_sms:
  name: 'Số điện thoại sms'
  icon: mdi:contact-phone
  
alarm_message:
  name: 'Nội dung tin nhắn'
  icon: mdi:sign-text 
```

```
# input_boolean.yaml
alarm_call:
  name: Gọi điện thoại
  icon: mdi:phone-in-talk

alarm_sms:
  name: Gửi tin nhắn
  icon: mdi:message-processing  
```

```
# input_number.yaml
alarm_call_repeat:
    name: Số lần gọi
    # initial: 1
    min: 1
    max: 5
    step: 1
    icon: mdi:phone-plus 
```

```
# automations.yaml
- alias: alarm gateway make call
  trigger:
    platform: state
    entity_id: 
      - sensor.alarm_sensor 
    to: 'on'
  condition:
    - condition: state
      entity_id: input_boolean.alarm_call
      state: 'on'    
  action:
    - service: alarm_gateway.call
      data_template:
        phone_numbers: >
          {{ states.input_text.alarm_phones_call.state }}
        call_repeat: > 
          {{ states.input_number.alarm_call_repeat.state | int }}
#---
- alias: alarm gateway send sms
  trigger:
    platform: state
    entity_id: 
      - sensor.alarm_sensor
    to: 'on'
  condition:
    - condition: state
      entity_id: input_boolean.alarm_sms
      state: 'on'    
  action:
    - service: alarm_gateway.send_sms
      data_template:
        phone_numbers: >
          {{ states.input_text.alarm_phones_sms.state }}
        message: >
          {{ states.input_text.alarm_message.state }}
```          

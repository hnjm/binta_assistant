# Binta assistant
Binta assitant is a personnal assistant that allows you to manage Odoo ERP with voice recognition technologies It uses NLP to extract and processing voice command, it build for the  master degree's theses in computer science's methods applied to a business management


## how to use it ?
the important thing to know before using Binta is that it's a client server application based on websocket protocol

### running Binta server 
 to recognize voice, you should run the server.py into rs_core folder like this
 `python server.py`
 
### running client 
 once server runing you have to run client also witch must listening the websocket server that started earlier,
 note that you can build your application completly in client.py file 
 ---
 
 Binta is build on Vosk that is an offline open source speech recognition toolkit to look it click here [github Vosk repository](https://github.com/alphacep/vosk-api)
 
 

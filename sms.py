from twilio.rest import Client 
 
account_sid = 'ACbdef92c2dd4f63d64e952992efe21465' 
auth_token = 'dbc3fd4ac3fa1815901f50d7fd3db1f9' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              from_='+12018826993', 
                              body='HEY! you gotta work harder. THIS IS ME FROM THE ZTM TEXTER - SRISHTI ',      
                              to='+919354467701' 
                          ) 
 
print(message.sid)
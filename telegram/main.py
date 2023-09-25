import requests

telegram_token = '6344692030:AAH-MG5ziOT4C-bnn9LqusVPN8UYqjBPDp0'
chat = 'testforyt2023'



def send_message(text):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    querystring = {"chat_id":f"@{chat}","text":text}
    response = requests.post(url, params=querystring)
    print(response.status_code)


if __name__ == '__main__':
    text = input('What text what you want to send? ')
    send_message(text)
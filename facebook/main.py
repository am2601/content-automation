import requests

PAGE_ID = '100438819483809'
TOKEN = 'EAAdb4S8dpZBABOwprueicNWlYZBaxDkPkAnyBGZCkSQXT8NwGhldSO2btngZAgkTH39ZA9vAekQC48Jyv0z2tZAB572ih66nBSFDTCB3khKQk8YM1QnKhDEMJzl2F0YBlYjlKwcQuFZCplyE1247exXgk3gVh3ZBPrXEZAmKeUBlxfwuv4hhB4n8yy7LbW5v2CR1bjomQYrlCjoyDCjOcsQRC4Kf7ZBTEpS7AG2PzOllUZD'

def post_to_page(text):
    url = f'https://graph.facebook.com/v18.0/{PAGE_ID}/feed?message={text}&access_token={TOKEN}'
    r = requests.post(url)
    return r.status_code

if __name__ == '__main__':
    code = post_to_page('Text from python')
    print(code)

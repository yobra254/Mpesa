import requests
import keys
from accesstoken import generate_access_token

my_access_token = generate_access_token()

def register_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {
        "ShortCode": keys.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://mydomain.com/confirmation",
        "ValidationURL": "https://mydomain.com/validation",
     }
    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)
#register_url()

def simulate_c2b_transaction():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {
        "ShortCode": keys.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "1",
        "Msisdn": "254795075791",
        "BillRefNumber": "12345678",
     }
    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)

simulate_c2b_transaction()
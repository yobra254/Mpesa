
import requests
import keys
from accesstoken import generate_access_token
from encode import generate_password
from utils import get_timestamp

my_access_token = generate_access_token()
formatted_time = get_timestamp()
decoded_password = generate_password(formatted_time)


def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
         "BusinessShortCode": keys.business_shortcode,
         "Password": decoded_password,
         "Timestamp": formatted_time,
         "TransactionType": "CustomerPayBillOnline",
         "Amount": 1,
         "PartyA": keys.phone_number,  # replace with your phone number to get stk push         
         "PartyB": keys.business_shortcode,
         "PhoneNumber": keys.phone_number,  # replace with your phone number to get stk push
         "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
         "AccountReference": "Brian",
         "TransactionDesc": "Testing stk push"
     }
    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)

lipa_na_mpesa()
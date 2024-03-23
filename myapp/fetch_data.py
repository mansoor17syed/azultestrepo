import requests
import time


def url_data():
    try:
        url = "https://api.coinbase.com/v2/exchange-rates"
        response = requests.get(url)
        data = response.json()
        # response_code = response.status_code
        
        cntry_name = ['INDIA', 'SAUDI ARABIA','CZECH REPUBLIC']
        cntry_code = ['INR', 'SAR','CZK']
        cntry_crr_INR = data['data']['rates']['INR']
        time.sleep(2)
        cntry_crr_SAR = data['data']['rates']['SAR']
        time.sleep(2)
        cntry_crr_CZK = data['data']['rates']['CZK']
        time.sleep(2)
        cntry_crr=[cntry_crr_INR,cntry_crr_SAR,cntry_crr_CZK]
        
        return [cntry_name,cntry_code,cntry_crr]
    
    except requests.exceptions.RequestException as errex:
        print("Unable to curl to url check network/connectivity of your env")
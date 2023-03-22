import urllib.request

def lambda_handler(event, context):
    # fetch the public IP address using urllib
    with urllib.request.urlopen('https://api.ipify.org') as response:
        ip_address = response.read().decode('utf-8')
    
    # print the public IP address
    print(f"My public IP address is {ip_address}")

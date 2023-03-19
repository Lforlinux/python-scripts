import requests
import random
import string
# here the requirement is 5 letter domain ends with ta.com
def generate_random_domain():
    letters = string.ascii_lowercase
    domain_name = ''.join(random.choice(letters) for i in range(3)) + "ta.com"
    return domain_name


def check_domain_availability(domain_name):
    api_key = "" # replace with your API key
    endpoint = f"https://domain-availability.whoisxmlapi.com/api/v1?apiKey={api_key}&domainName={domain_name}&outputFormat=JSON"
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        if data.get('DomainInfo').get('domainAvailability') == 'AVAILABLE':
            print(f"The domain {domain_name} is available for purchase!")
        else:
            print(f"Sorry, the domain {domain_name} is already taken.")
    elif response.status_code == 401:
        print("Invalid API key. Please check your API key and try again.")
    elif response.status_code == 404:
        print("The API endpoint could not be found. Please check the URL and try again.")
    else:
        print(f"Oops! Something went wrong. Error code: {response.status_code}")



# Generate 10 random domain names and check their availability
domain_names = [generate_random_domain() for i in range(10)]

for domain_name in domain_names:
    if check_domain_availability(domain_name):
        print(f"The domain {domain_name} is available for purchase!")
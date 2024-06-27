import requests
from bs4 import BeautifulSoup
import pandas as pd
import pickle
from time import sleep

# def fetch_url(url, retries=7, backoff_factor=1):
#     for i in range(retries):
#         try:
#             response = requests.get(url)
#             if response.status_code == 200:
#                 return response.text
#             else:
#                 print(f"Received status code {response.status_code}")
#         except requests.exceptions.RequestException as e:
#             print(f"Request failed: {e}")
#         sleep(backoff_factor * (2 ** i))  # Exponential backoff
#     return None

# Base URL for Hugging Face models
base_url_part_1 = "https://huggingface.co/models?p="
base_url_part_2 = "&sort=trending"
#24528
model_names_all = []
for i in range(1226*2, 1226*3):
    url = base_url_part_1 + str(i) + base_url_part_2
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    model_names = soup.find_all('h4')
    #Remove the html tags
    model_names = [model.get_text() for model in model_names]
    model_names_all.extend(model_names)
    print(i)
print(len(model_names_all))
# Save the model names to a pickle file
with open('model_names.pkl', 'ab') as f:
    pickle.dump(model_names_all, f)

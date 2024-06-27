import requests
from bs4 import BeautifulSoup
import pandas as pd
import pickle

# Base URL for Hugging Face models
base_url_part_1 = "https://huggingface.co/models?p="
base_url_part_2 = "&sort=trending"
#24528
model_names_all = []
for i in range(1226*5, 1226*6):
    url = base_url_part_1 + str(i) + base_url_part_2
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    model_names = soup.find_all('h4' , class_ = 'text-md truncate font-mono text-black dark:group-hover/repo:text-yellow-500 group-hover/repo:text-indigo-600 text-smd')
    #Remove the html tags
    model_names = [model.get_text() for model in model_names]
    model_names_all.extend(model_names)
    print(i)
print(len(model_names_all))
# Save the model names to a pickle file
with open('model_names.pkl', 'ab') as f:
    pickle.dump(model_names_all, f)

import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import json
import csv

base_url = "https://health-diet.ru"

# this part goes to the web page, gets its content and saves it into the file
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

# req = requests.get(url, headers=headers)
# src = req.text
#
# with open("index.html", "w", encoding='utf-8') as file:
#     file.write(src)


# This part gets all links that we need to parse and saves it into json file
# with open("index.html", encoding='utf-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# links = user_name = soup.find_all("a", class_="mzr-tc-group-item-href")
#
# all_categories_dic = {}
# for link in links:
#     full_link = base_url + link.get("href")
#     link_text = link.text
#     print(link_text, " - ", full_link)
#
#     all_categories_dic[link_text] = full_link
#
# with open("all_categories_dic.json", "w", encoding='utf-8') as file:
#     json.dump(all_categories_dic, file, indent=4, ensure_ascii=False)


with open("all_categories_dic.json", encoding='utf-8') as file:
    all_categories = json.load(file)

iteration_count = int(len(all_categories) - 1)
count = 0
print(f"There were iterations: {iteration_count}")

for category_name, category_href in all_categories.items():

    rep = [",", " ", "-", "'"]
    for sym in rep:
        if sym in category_name:
            category_name = category_name.replace(sym, "_")

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"info/{count}_{category_name}.html", "w", encoding='utf-8') as file:
        file.write(src)

    with open(f"info/{count}_{category_name}.html", encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # checking page for existing table
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    # lets get titles of the table
    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fat = table_head[3].text
    carbs = table_head[4].text

    # writing titles into file
    # with open(f"info/{count}_{category_name}.csv", "w", encoding='utf-8-sig') as file:
    #     writer = csv.writer(file)
    #     writer.writerow((
    #         product,
    #         calories,
    #         proteins,
    #         fat,
    #         carbs
    #     ))

    # getting data of products
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    product_info = []

    for prod in products_data:
        product_tds = prod.find_all("td")
        title = product_tds[0].find("a").text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fat = product_tds[3].text
        carbs = product_tds[4].text

        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fat": fat,
                "Carbs": carbs
            }
        )

        # with open(f"info/{count}_{category_name}.csv", "a", encoding='utf-8-sig') as file:
        #     writer = csv.writer(file)
        #     writer.writerow((
        #         title,
        #         calories,
        #         proteins,
        #         fat,
        #         carbs
        #     ))
    with open(f"info/{count}_{category_name}.json", "a", encoding="utf-8-sig") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"# Iteration {count}. {category_name} has been written")
    iteration_count = iteration_count - 1
    if iteration_count == 0:
        print("The process has been finished")
        break

    print(f"Iterations left: {iteration_count}")
    sleep(random.randrange(2, 4))

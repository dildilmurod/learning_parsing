import re

from bs4 import BeautifulSoup

with open("info/index2.html", encoding='utf-8') as file:
    src = file.read()

# print(src)

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title.text)

# page_h1 = soup.find("h1")
# print(page_h1)
#
# page_all_h1 = soup.find_all("div")
# # print(page_all_h1)
#
# for item in page_all_h1:
#     print(item.text)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find("div", class_="user__name").find("span").text
# print(user_name)


# user_name = soup.find("div", {"class": "user__name", "id"}).find("span").text.strip()
# print(user_name)

# find_all_spans = soup.find(class_="user__info").find_all("span")
#
# for item in find_all_spans:
#     print(item.text)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_links)

#getting links from page
# all_a = soup.find_all("a")
# for item in all_a:
#     url = item.get("href")
#     print(f"{item.text}: {url}")

# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# next_el = soup.find(class_="post__title").next_element.next_element.text
# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)

#this does not work, as bsoup can not find by part of the text
# find_a = soup.find("a", text="Одежда")

# find_a = soup.find("a", text="Одежда для взрослых")
# print(find_a)
#
# another way is to implement re.complite to use reg exp
# find_a_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_text)
#
# find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_all_clothes)


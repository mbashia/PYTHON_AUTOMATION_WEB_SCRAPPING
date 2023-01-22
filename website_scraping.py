from bs4 import BeautifulSoup
import requests
import time

print("enter the skill that you are unfamiliar with...")
unfamiliar_skill = input('>')
print(F'filtering out {unfamiliar_skill}...')


def results():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    for job in jobs:
        published_date = job.find("span", class_="sim-posted").span.text
        if 'few ' in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a['href']
            # the method above is used to access attributes eg. a['href']
            # print(published_date)
            if unfamiliar_skill not in skills:
                with open("post.txt", 'a') as f:
                    f.write(f'company_name : {company_name.strip()}\n')
                    f.write(f'skills:{skills.strip()}\n')
                    f.write(f'more_info:{more_info}\n')
                    f.write("\n")
                print("FILE SAVED!")


if __name__ == "__main__":
    # while True:
        results()
        print("wait for ten minutes for the next resutlt...")
        time.sleep(600)

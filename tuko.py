import requests
from bs4 import BeautifulSoup 

response = requests.get('https://www.tuko.co.ke')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    sections = soup.find_all('section')

    for idx, section in enumerate(sections):
        print(f"section {idx + 1}: \n\t")
        articles = section.find_all('article')
        if articles:
            for article in articles:
                anchor =  article.find('a')
                if anchor:
                    headline = anchor.get_text(strip=True)   

                    link = anchor.get('href')
                    print(f"Link: {link}")
                    print(f"headline: {headline}")
                    




    #print(soup.prettify())
    #data = soup.find_all('article', class_ = 'c-article-card-main')

    
    # if data:
    #     for article in data:
    #         links = article.find_all('a', class_ = 'c-article-card-main__headline')
    #         for link in links:
    #             print(link.get('href'))
    #             h = link.find('span', '')
    #    -         print(h)
    

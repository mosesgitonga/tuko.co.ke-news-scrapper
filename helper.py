from bs4 import BeautifulSoup
import requests

class Helper():
    def __init__(self):
        pass

    @staticmethod
    def get_full_article(link, headline=None):
        # Send request to the provided article URL
        response = requests.get(link)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            article = soup.find('article', class_="post__main js-article-body")
            if article:
                headline = article.h1.text if article.h1 else "No headline found"
                
                # Remove unwanted elements
                call_to_actions = article.find_all('div', class_="call_to_action")
                for c in call_to_actions:
                    c.decompose()
                
                read_alsos = article.find_all('a', class_="c-article-read-also__headline")
                for read_also in read_alsos:
                    read_also.decompose()
                
                paragraphs = article.find_all('p', class_="align-left")
                clean_article = []

                for p in paragraphs:
                    clean_article.append(f'{p.get_text(strip=True)}\n')
                
                return ''.join(clean_article), headline
            else:
                return "Article body not found."
        else:
            return f"Failed to retrieve the article. Status code: {response.status_code}"
            





if __name__ == "__main__":
    helper = Helper()
    link = "https://kiswahili.tuko.co.ke/siasa/575039-william-ruto-aondoka-nchini-kuelekea-uganda-jinsi-kenya-itakavyofaidika/"
    x = helper.get_full_article(link)
    print(x)
import requests


def card():
    url = 'https://sites.google.com/d/18h-YjT0ulJT4a93e21STAwFUaEBfrc-t/p/1CvX965mVqtwe1hOKBffaMC1y9OGOGTAi/edit?pli=1'
    response = requests.get(url)
    print = response

if __name__=="__main__":
    card()
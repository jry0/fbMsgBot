from bs4 import BeautifulSoup
import requests

def getBeeMovieScript():
    source = requests.get("https://sites.google.com/a/ausdg.us/force-and-motion/the-entire-bee-movie-script").text
    # Uses python default html parser, can switch to faster alt. later
    soup = BeautifulSoup(source, "html.parser")  
    beeScript = soup.find_all('div', dir= "ltr")[23].text   # There could be a better solution than this, such as creating own find conditions (function)
                                                        # Had to sift thru garbage website littered with profanities 
    return beeScript

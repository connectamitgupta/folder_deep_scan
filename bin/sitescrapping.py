################ 

# import requests

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)

# print(page.text)


#############################################################

# import requests
# from bs4 import BeautifulSoup

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify())


############################################################

from pywebcopy import save_webpage
 
kwargs = {'project_name': 'site folder'}
 
save_webpage(
   
    # url of the website
    url='http://yuvafitnessplus.com/',
     
    # folder where the copy will be saved
    project_folder='D:\Clientproject\YuvaFitnessPlus\Oldwebsite\ThroughPython',
    **kwargs
)
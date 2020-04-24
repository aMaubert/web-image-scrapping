# Web Image Scrapping

Web Scrapping d'images . 

## Pré-requis 

Il faut avoir l'executable [ChromeDriver](https://chromedriver.chromium.org/downloads)  
Cet executable est un WebDriver pour Chorme.  
Attention de télecharger le bon driver en fonction de la version de chrome que vous utilisez.
## Install dependecies

````shell script
pip install -r requirements.txt
````

## Example

We will suppose the values : 

```
keyword = the keyword you search for
/path/to/chromedriver = the absolute path to your chromedriver
300 = the number of images you want to download
/path/to/your/output/repository = the absolute path to your output repository, where you want you images downloaded

```

````shell script
python3 crasping.py keyword \
         /path/to/chromedriver \
         300 \
        /path/to/your/output/repository
````
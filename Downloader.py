import requests
from os import path
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Downloader:
    def __init__(self, output_directory):
        if not path.exists(output_directory):
            print('Images folder : ', output_directory, ' doesn\'t exist.', file=sys.stderr)
            exit(1)
        elif not path.isdir(output_directory) :
            print(output_directory, ' is\'nt a folder.', file=sys.stderr)
            exit(1)
        self.output_directory = output_directory

    def download_images(self, urls: []):
        counter = 0

        for eachUrl in urls:
            counter += 1
            local_path = self.output_directory + "/" + str(counter) + ".jpg"
            self.download_image(eachUrl, local_path)
        print( str(len(urls)), ' image(s) downloaded .')

    def download_image(self, download_src, local_path):
        try:
            response = requests.get(download_src, verify=False, stream=True)
            raw_data = response.raw.read()
            with open(local_path, 'wb') as file:
                file.write(raw_data)
        except Exception as e:
            print(f'No found image sources.')
            print(e)
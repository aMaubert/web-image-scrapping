#!/usr/bin/python
from Arguments import Arguments
from Browser import Browser
from Downloader import Downloader
from ImageEditor import ImageEditor

import os

def main( args: Arguments):
    print(args)
    downloader = Downloader(args.output_directory)
    browser = Browser(args.webdriver, args.max_images, args.keyword)
    urls = browser.launchSearch()
    downloader.download_images(urls)
    for file in os.listdir(args.output_directory) :
        if file.endswith('.jpg') :
            image_editor = ImageEditor(file_path= args.output_directory + '/' + file )
            #convert_mode= 'RGB' => RGB or 'L'=> greyscale
            image_editor.resize( size=(64, 64), convert_mode='RGB')



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Create a schema')
    parser.add_argument('key_word', type=str, help='the search keyword .')
    parser.add_argument('output_directory',type=str,  help='the path to the output directory')
    parser.add_argument('max_images', type=int, help='the number maximum of images to download')
    parser.add_argument('webdriver_path',  help='The path of the webdriver', type=str)
    args = parser.parse_args()
    args = Arguments( args.key_word, args.output_directory, args.webdriver_path, args.max_images )
    main(args)

class Arguments:

    """Class for arguments"""
    def __init__(self, keyword: str, webdriver, output_directory, max_images):
        if keyword.find(' ') == 0 :
            keyword.replace(' ', '+')
        self.keyword = keyword
        self.webdriver = webdriver
        self.output_directory = output_directory
        self.max_images = max_images

    def __str__(self):
        return 'Arguments( keyword=' + self.keyword+\
                         ', webdriver=' + self.webdriver +\
                         ', output_directory=' + self.output_directory +\
                         ', max_images=' + str(self.max_images) + ')'
    def __repr__(self):
        return {'keyword' :self.keyword ,'name':self.webdriver, 'output_directory' : self.output_directory, 'max_images' : self.max_images}
import os
import shutil


def main() :
    directory_target_path = '/Users/allan/Documents/ESGI/4AL/deep-learning/project/sign-it/dataset/obligation'
    count_file_number = 1
    for directory_path, directories, files in os.walk(directory_target_path) :
        print(directory_path)
        for eachFile in files:
            print('file : ', directory_path  + '/' + eachFile)
            shutil.copy(directory_path  + '/' + eachFile, directory_target_path + '/' + str(count_file_number) + '.jpg')
            count_file_number += 1


if __name__ == '__main__':
    main()
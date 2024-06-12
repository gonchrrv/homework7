from zipfile import ZipFile

with ZipFile('tmp/Hello World.zip') as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('Hello.txt')
    print(text)
    zip_file.extract('Hello.txt', 'resources')
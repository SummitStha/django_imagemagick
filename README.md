# django_imagemagick
This repository contains a simple example project that is used to generate the thumbnail of a document automatically and then saves the thumbnail in the database

## Installation
Install ImageMagick for Ubuntu
```
sudo apt-get install libmagickwand-dev imagemagick libmagickcore-dev
```

Install ImageMagick for Mac:
```
brew update
brew install imagemagick
```

## Update the ImageMagick policy file
In file /etc/ImageMagick-6/policy.xml (or /etc/ImageMagick/policy.xml)
1. Comment out the line
```
<!-- <policy domain="coder" rights="none" pattern="MVG" /> -->
```
2. Change the line
```
<policy domain="coder" rights="none" pattern="PDF" />
```
to
```
<policy domain="coder" rights="read|write" pattern="PDF" />
```
3. Add a new line
```
<policy domain="coder" rights="read|write" pattern="LABEL" />
```

## Install the requirements and run the project
```
pip install -r requirements.txt
python manage.py runserver 
```

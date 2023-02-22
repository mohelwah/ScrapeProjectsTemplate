[![ScrapeTemplate](https://github.com/mohelwah/ScrapeProjectsTemplate/actions/workflows/main.yml/badge.svg)](https://github.com/mohelwah/ScrapeProjectsTemplate/actions/workflows/main.yml)

# Project Type: Scrape Project Template
# Project Name : Template

this is scaffold template for scrape project in python 
 Create the following:
 - Makefile
 - requirement.txt
 -Linux system:
    - virtial enviroment: python -m venv ~/.scrape
    - activate venv envi: source ~/.scrape/bin/activate
 - Windows system:
    - virtial enviroment: python -m venv c:\venv\scrapy
    - activate venv envi:   C:\venv\scrapy\Scripts\activate.ps1
 - hello.py file
 - test_hello.py file 
 - to check the python version:
    - in linux : which python  
    - in windows: Get-Command python | fl *
 - get pack list:
    - pip freeze or pip list 
    test
<<<<<<< HEAD
=======
## To run selenuim in github codespace
-  sudo apt-get updata 
- apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb
* install chrome 
- wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
- sudo apt install ./google-chrome-stable_current_amd64.deb

## run jupyter notebook
  - jupyter noteboke: - install ipykernel
        run command: - ipython kernel install --user --name=scrape
       
       

## To run selenuim in github codespace
-  sudo apt-get updata 
- apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb
* install chrome 
- wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
- sudo apt install ./google-chrome-stable_current_amd64.deb

## run jupyter notebook
  - jupyter noteboke: - install ipykernel
        run command: - ipython kernel install --user --name=scrapy
>>>>>>> 129098bff92a0a876e004e0c252fd6df859a0bae

# To start a new Scrapy project, follow these steps:

Open a terminal or command prompt on your computer.

Install Scrapy using pip. Run the following command:

 create a new Scrapy project using the scrapy startproject command. Choose a name for your project and replace project_name with your chosen name. For example, to create a project named myproject, use the following command:


> scrapy startproject myproject
Scrapy will create a new project directory with the same name as your project. Navigate into the project directory using the cd command:

> cd myproject
Once inside the project directory, you'll see several files and directories, including a spiders directory. This directory will contain your spiders, which are Python scripts that define how to scrape data from a website. To create a new spider, run the following command:


> scrapy genspider spider_name website.com
Replace spider_name with a name for your spider and website.com with the domain name of the website you want to scrape. For example, to create a spider named example for the website example.com, use the following command:


> scrapy genspider example example.com
Scrapy will create a new spider file in the spiders directory. Open this file in a text editor and define how to extract data from the website.

That's it! You've now started a new Scrapy project and created a spider to scrape data from a website. You can run the spider using the scrapy crawl command followed by the name of the spider.



# Here are the steps to run a Scrapy project:

Open a terminal or command prompt and navigate to the root directory of your Scrapy project.


Run the Scrapy command to start the spider. To run the spider, use the following command:


> scrapy crawl spider_name
Replace spider_name with the name of the spider you want to run.

Wait for the spider to finish crawling. The spider will output log messages to the terminal as it crawls. You should see messages indicating the spider is crawling URLs and extracting data.

Check the output. Scrapy can output the results in various formats, including CSV, JSON, and XML. By default, Scrapy outputs the results to the console. If you want to save the results to a file, you can use the -o option followed by the filename and extension. For example, to save the results to a CSV file, use the following command:


scrapy crawl spider_name -o output.csv
This will save the results to a file named output.csv in the same directory as the Scrapy project.

# Adding new spiders 
When you create a new Scrapy project using the scrapy startproject command, Scrapy automatically generates a directory structure for your project. One of the directories it creates is called spiders, and this is where you should place your Spider files.

So, when you create a new Spider using the scrapy genspider command, Scrapy will generate a new Python file with the Spider code inside it. This file should be saved in the spiders directory.

For example, if you created a Scrapy project called myproject, and then created a Spider called example for the website example.com using the following command:

Copy code
scrapy genspider example example.com
Scrapy would generate a new Python file called example.py and save it in the myproject/spiders/ directory. You can open this file in a text editor to see the Spider code, and modify it to suit your needs.

Note that you can create as many Spider files as you need in the spiders directory, and you can also organize your code into subdirectories within the spiders directory if you prefer. Just make sure that any new Spider files you create are saved in the spiders directory, and that their names end with the .py extension.
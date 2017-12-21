# CS410_Search_Engine

Our team has built a car search engine which is quite different from traditional car search engines. Normally, a car website will ask you to choose the brand, make and price, and then recommend the cars to you. However, this is actually not that applicable to people who are not familiar with cars. For example, if a mother wants to buy a car which is comfortable for babies, she may not care about the car make. So basically our search engine targets at these people.

There are 3 parts of developments in this project. Firstly, we need to collect car data to form the collection, and we decide to use web crawling techniques. Next thing is to build index on this collection, as well as implement the proper ranking function. Finally, we must create an UI to make this search engine user friendly.

In this project, we use python library BeautifulSoup to do web crawling. We have browsed several car websites such as www.car.com, and we finally choose to collect data from www.sgcarmart.com as it contains both car info and customer reviews. The web_crawler.py file is written for this purpose.

After generating the cardata.dat file, one more step needed is to do data cleaning. The reason is, for this website, it will use “unknown” or “no” to indicate those missing car specs and features. For dictionary construction purpose, we need to remove those words.

Once the cardata.dat file is finalized, we proceed to build index on it by using library Metapy, which is introduced during assignments so we are quite familiar with. One thing to take note is, since we need to know the exact content of each document, we must add “store-full-text = true” parameter inside line.toml file for preparation. While building index, we use the same settings in config.toml file from previous assignments, namely, same stopwords.txt file and default unigram method, this should be efficient and effective enough to implement the algorithm. Regarding the most suitable ranking function, our final decision is to use BM25, and we would like to show the first 10 records returned.

The last step is to create a UI to present the results. We choose tkinter library, a standard GUI package in this case. The interface is quite similar to google search engine, which shows a blank search bar in the middle for users to input any query. After backend algorithm retrieves 10 most relevant records, the corresponding website links will be displayed sequentially. When users click on one of the URLs, he or she will be redirected to the website with full information of the specific car.

To use our car search engine, you may download the whole batch of files from Github repository, and run the python file car.py directly. You may type in queries such as “most comfortable car”, “built in Japan” etc., and then click on the link returned to browse the website for more information.

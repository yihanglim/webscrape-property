# Webscraping Project

## Introduction
This project is a webscraping tool for a property website in Malaysia. This project mainly lies on Django framework, with Mongodb as database, 
Rest API, Ajax for dynamic loading on the frontend and python beautifulsoup as webscraping tool.

### Working Model 
https://webscrape-property.herokuapp.com/<br/>

![alt text](https://github.com/yihanglim/webscrape-property/blob/master/front_page.PNG)

Button function on the front page<br/>
**"Source code"**: The link to the source code on github<br/>

**"Get from database"**: Load the property data from the database, this might take a while when the database getting larger, due to all data will be load on one page. Can be fixed in future by adding multiple page.<br/>

**"Scrape"**: Run a POST API to call the scrape function, this will take apporximately 1 minute or less to execute, once the scraping is done, the page will re-render the page with all the data from databse by sorting the latest data on the top.<br/>

**"Export to CSV"**: Export to csv for the scraped data. (currently not working well on the demo due to heroku static file restriction)<br/>

**"Edit"**: Aim to open a Modal prompt to view and edit property detail. (still in development)<br/>

**"Delete"**: Delete the target property<br/>

### Webscraping part  

User Agent is used to avoid detected by anti web-scraping bots, but unfortunately still couldn't overcome the anti webscraping bots. The scraping will run at most 4 request at the same time before being blocked.  

The block will b reset after few hours or use a different IP address.  

The *def scrape()* will loop through each page of the webstie at "Rent" page, to scrape for all rental properties. As mentioned, with only 4 requests before being block, it can only scrape for 4 pages.  

It first parse the url's html page with beautifulsoup, and then loop through each listing from *div class="listing-card"*  

For every listing, all the parameter (links, address, state, names, prices, bedrooms, bathrooms, built_ups, built_years, house_types, furnishings, price_per_sqft, images link) will be store in a List.  

Once the scraping is done, all the parameter list will be convert to a list of dictionary before passing into database.  

A csv file will be generated to be used for other purpose or as backup in case of database storing fail.  


### API  
This project use DJjango with Rest Framework, the API include GET for fetching data from database, POST for create data in database, PUT for update database data, DELETE for delete data.  
Thanks to Django framework that makes serializing simple, as in *serializer.py*  

### Database  

The database used in this is Mongodb hosted on AWS free tier server.  
Djongo package is used as connector between Django and Mongodb.  


### Frontend  
The front end is a simple html page, with a little of CSS styling and Ajax to load content dynamically  
Key process of Ajax  
PROCESS:
			1 - Fetch Data and build rows "buildList()"  
			2 - Call scrape API to activate data scraping  
			3 - Edit Item - to edit item's detail (still in progress)  
			4 - Delete Item - Send item id to delete URL  
      5 - Use eventhandler to edit and delete
      6 - CSRF Token  

### Steps to run this:  

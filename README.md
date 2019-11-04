# Web_Scraping_Mission-to-Mars

Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter are used to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page
## Step 1 - Scraping
### NASA Mars News
* Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

### JPL Mars Space Images - Featured Image
Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

### Mars Weather

Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. 

### Mars Facts

Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
* Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
* Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

### Some screenshot from the project

![Image description](https://github.com/melakue/Web_Scraping_Mission-to-Mars/blob/master/Index.PNG)


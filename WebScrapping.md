```python
from bs4 import BeautifulSoup as bs
import requests
import pandas

'https://books.toscrape.com/catalogue/page-46.html'

'https://books.toscrape.com/'
```


```python
html_page = requests.get('https://books.toscrape.com/')
soup = bs(html_page.content, 'html.parser')
```


```python
soup.prettify
```




    <bound method Tag.prettify of <!DOCTYPE html>
    
    <!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
    <!--[if IE 7]>         <html lang="en-us" class="no-js lt-ie9 lt-ie8"> <![endif]-->
    <!--[if IE 8]>         <html lang="en-us" class="no-js lt-ie9"> <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en-us"> <!--<![endif]-->
    <head>
    <title>
        All products | Books to Scrape - Sandbox
    </title>
    <meta content="text/html; charset=utf-8" http-equiv="content-type"/>
    <meta content="24th Jun 2016 09:29" name="created"/>
    <meta content="" name="description"/>
    <meta content="width=device-width" name="viewport"/>
    <meta content="NOARCHIVE,NOCACHE" name="robots"/>
    <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
    <!--[if lt IE 9]>
            <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
            <![endif]-->
    <link href="static/oscar/favicon.ico" rel="shortcut icon"/>
    <link href="static/oscar/css/styles.css" rel="stylesheet" type="text/css"/>
    <link href="static/oscar/js/bootstrap-datetimepicker/bootstrap-datetimepicker.css" rel="stylesheet"/>
    <link href="static/oscar/css/datetimepicker.css" rel="stylesheet" type="text/css"/>
    </head>
    <body class="default" id="default">
    <header class="header container-fluid">
    <div class="page_inner">
    <div class="row">
    <div class="col-sm-8 h1"><a href="index.html">Books to Scrape</a><small> We love being scraped!</small>
    </div>
    </div>
    </div>
    </header>
    <div class="container-fluid page">
    <div class="page_inner">
    <ul class="breadcrumb">
    <li>
    <a href="index.html">Home</a>
    </li>
    <li class="active">All products</li>
    </ul>
    <div class="row">
    <aside class="sidebar col-sm-4 col-md-3">
    <div id="promotions_left">
    </div>
    <div class="side_categories">
    <ul class="nav nav-list">
    <li>
    <a href="catalogue/category/books_1/index.html">
                                
                                    Books
                                
                            </a>
    <ul>
    <li>
    <a href="catalogue/category/books/travel_2/index.html">
                                
                                    Travel
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/mystery_3/index.html">
                                
                                    Mystery
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/historical-fiction_4/index.html">
                                
                                    Historical Fiction
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/sequential-art_5/index.html">
                                
                                    Sequential Art
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/classics_6/index.html">
                                
                                    Classics
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/philosophy_7/index.html">
                                
                                    Philosophy
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/romance_8/index.html">
                                
                                    Romance
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/womens-fiction_9/index.html">
                                
                                    Womens Fiction
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/fiction_10/index.html">
                                
                                    Fiction
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/childrens_11/index.html">
                                
                                    Childrens
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/religion_12/index.html">
                                
                                    Religion
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/nonfiction_13/index.html">
                                
                                    Nonfiction
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/music_14/index.html">
                                
                                    Music
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/default_15/index.html">
                                
                                    Default
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/science-fiction_16/index.html">
                                
                                    Science Fiction
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/sports-and-games_17/index.html">
                                
                                    Sports and Games
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/add-a-comment_18/index.html">
                                
                                    Add a comment
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/fantasy_19/index.html">
                                
                                    Fantasy
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/new-adult_20/index.html">
                                
                                    New Adult
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/young-adult_21/index.html">
                                
                                    Young Adult
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/science_22/index.html">
                                
                                    Science
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/poetry_23/index.html">
                                
                                    Poetry
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/paranormal_24/index.html">
                                
                                    Paranormal
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/art_25/index.html">
                                
                                    Art
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/psychology_26/index.html">
                                
                                    Psychology
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/autobiography_27/index.html">
                                
                                    Autobiography
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/parenting_28/index.html">
                                
                                    Parenting
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/adult-fiction_29/index.html">
                                
                                    Adult Fiction
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/humor_30/index.html">
                                
                                    Humor
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/horror_31/index.html">
                                
                                    Horror
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/history_32/index.html">
                                
                                    History
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/food-and-drink_33/index.html">
                                
                                    Food and Drink
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/christian-fiction_34/index.html">
                                
                                    Christian Fiction
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/business_35/index.html">
                                
                                    Business
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/biography_36/index.html">
                                
                                    Biography
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/thriller_37/index.html">
                                
                                    Thriller
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/contemporary_38/index.html">
                                
                                    Contemporary
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/spirituality_39/index.html">
                                
                                    Spirituality
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/academic_40/index.html">
                                
                                    Academic
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/self-help_41/index.html">
                                
                                    Self Help
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/historical_42/index.html">
                                
                                    Historical
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/christian_43/index.html">
                                
                                    Christian
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/suspense_44/index.html">
                                
                                    Suspense
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/short-stories_45/index.html">
                                
                                    Short Stories
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/novels_46/index.html">
                                
                                    Novels
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/health_47/index.html">
                                
                                    Health
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/politics_48/index.html">
                                
                                    Politics
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/cultural_49/index.html">
                                
                                    Cultural
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/erotica_50/index.html">
                                
                                    Erotica
                                
                            </a>
    </li>
    <li>
    <a href="catalogue/category/books/crime_51/index.html">
                                
                                    Crime
                                
                            </a>
    </li>
    </ul></li>
    </ul>
    </div>
    </aside>
    <div class="col-sm-8 col-md-9">
    <div class="page-header action">
    <h1>All products</h1>
    </div>
    <div id="messages">
    </div>
    <div id="promotions">
    </div>
    <form class="form-horizontal" method="get">
    <div style="display:none">
    </div>
    <strong>1000</strong> results - showing <strong>1</strong> to <strong>20</strong>.
                    
                
                
            
        </form>
    <section>
    <div class="alert alert-warning" role="alert"><strong>Warning!</strong> This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.</div>
    <div>
    <ol class="row">
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>
    </div>
    <p class="star-rating Three">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
    <div class="product_price">
    <p class="price_color">£51.77</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/tipping-the-velvet_999/index.html"><img alt="Tipping the Velvet" class="thumbnail" src="media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg"/></a>
    </div>
    <p class="star-rating One">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/tipping-the-velvet_999/index.html" title="Tipping the Velvet">Tipping the Velvet</a></h3>
    <div class="product_price">
    <p class="price_color">£53.74</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/soumission_998/index.html"><img alt="Soumission" class="thumbnail" src="media/cache/3e/ef/3eef99c9d9adef34639f510662022830.jpg"/></a>
    </div>
    <p class="star-rating One">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/soumission_998/index.html" title="Soumission">Soumission</a></h3>
    <div class="product_price">
    <p class="price_color">£50.10</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/sharp-objects_997/index.html"><img alt="Sharp Objects" class="thumbnail" src="media/cache/32/51/3251cf3a3412f53f339e42cac2134093.jpg"/></a>
    </div>
    <p class="star-rating Four">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/sharp-objects_997/index.html" title="Sharp Objects">Sharp Objects</a></h3>
    <div class="product_price">
    <p class="price_color">£47.82</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/sapiens-a-brief-history-of-humankind_996/index.html"><img alt="Sapiens: A Brief History of Humankind" class="thumbnail" src="media/cache/be/a5/bea5697f2534a2f86a3ef27b5a8c12a6.jpg"/></a>
    </div>
    <p class="star-rating Five">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/sapiens-a-brief-history-of-humankind_996/index.html" title="Sapiens: A Brief History of Humankind">Sapiens: A Brief History ...</a></h3>
    <div class="product_price">
    <p class="price_color">£54.23</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/the-requiem-red_995/index.html"><img alt="The Requiem Red" class="thumbnail" src="media/cache/68/33/68339b4c9bc034267e1da611ab3b34f8.jpg"/></a>
    </div>
    <p class="star-rating One">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/the-requiem-red_995/index.html" title="The Requiem Red">The Requiem Red</a></h3>
    <div class="product_price">
    <p class="price_color">£22.65</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html"><img alt="The Dirty Little Secrets of Getting Your Dream Job" class="thumbnail" src="media/cache/92/27/92274a95b7c251fea59a2b8a78275ab4.jpg"/></a>
    </div>
    <p class="star-rating Four">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html" title="The Dirty Little Secrets of Getting Your Dream Job">The Dirty Little Secrets ...</a></h3>
    <div class="product_price">
    <p class="price_color">£33.34</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html"><img alt="The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull" class="thumbnail" src="media/cache/3d/54/3d54940e57e662c4dd1f3ff00c78cc64.jpg"/></a>
    </div>
    <p class="star-rating Three">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html" title="The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull">The Coming Woman: A ...</a></h3>
    <div class="product_price">
    <p class="price_color">£17.93</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html"><img alt="The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics" class="thumbnail" src="media/cache/66/88/66883b91f6804b2323c8369331cb7dd1.jpg"/></a>
    </div>
    <p class="star-rating Four">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html" title="The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics">The Boys in the ...</a></h3>
    <div class="product_price">
    <p class="price_color">£22.60</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/the-black-maria_991/index.html"><img alt="The Black Maria" class="thumbnail" src="media/cache/58/46/5846057e28022268153beff6d352b06c.jpg"/></a>
    </div>
    <p class="star-rating One">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/the-black-maria_991/index.html" title="The Black Maria">The Black Maria</a></h3>
    <div class="product_price">
    <p class="price_color">£52.15</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html"><img alt="Starving Hearts (Triangular Trade Trilogy, #1)" class="thumbnail" src="media/cache/be/f4/bef44da28c98f905a3ebec0b87be8530.jpg"/></a>
    </div>
    <p class="star-rating Two">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html" title="Starving Hearts (Triangular Trade Trilogy, #1)">Starving Hearts (Triangular Trade ...</a></h3>
    <div class="product_price">
    <p class="price_color">£13.99</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/shakespeares-sonnets_989/index.html"><img alt="Shakespeare's Sonnets" class="thumbnail" src="media/cache/10/48/1048f63d3b5061cd2f424d20b3f9b666.jpg"/></a>
    </div>
    <p class="star-rating Four">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/shakespeares-sonnets_989/index.html" title="Shakespeare's Sonnets">Shakespeare's Sonnets</a></h3>
    <div class="product_price">
    <p class="price_color">£20.66</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/set-me-free_988/index.html"><img alt="Set Me Free" class="thumbnail" src="media/cache/5b/88/5b88c52633f53cacf162c15f4f823153.jpg"/></a>
    </div>
    <p class="star-rating Five">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/set-me-free_988/index.html" title="Set Me Free">Set Me Free</a></h3>
    <div class="product_price">
    <p class="price_color">£17.46</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html"><img alt="Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)" class="thumbnail" src="media/cache/94/b1/94b1b8b244bce9677c2f29ccc890d4d2.jpg"/></a>
    </div>
    <p class="star-rating Five">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html" title="Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)">Scott Pilgrim's Precious Little ...</a></h3>
    <div class="product_price">
    <p class="price_color">£52.29</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/rip-it-up-and-start-again_986/index.html"><img alt="Rip it Up and Start Again" class="thumbnail" src="media/cache/81/c4/81c4a973364e17d01f217e1188253d5e.jpg"/></a>
    </div>
    <p class="star-rating Five">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/rip-it-up-and-start-again_986/index.html" title="Rip it Up and Start Again">Rip it Up and ...</a></h3>
    <div class="product_price">
    <p class="price_color">£35.02</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html"><img alt="Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991" class="thumbnail" src="media/cache/54/60/54607fe8945897cdcced0044103b10b6.jpg"/></a>
    </div>
    <p class="star-rating Three">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html" title="Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991">Our Band Could Be ...</a></h3>
    <div class="product_price">
    <p class="price_color">£57.25</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/olio_984/index.html"><img alt="Olio" class="thumbnail" src="media/cache/55/33/553310a7162dfbc2c6d19a84da0df9e1.jpg"/></a>
    </div>
    <p class="star-rating One">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/olio_984/index.html" title="Olio">Olio</a></h3>
    <div class="product_price">
    <p class="price_color">£23.88</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html"><img alt="Mesaerion: The Best Science Fiction Stories 1800-1849" class="thumbnail" src="media/cache/09/a3/09a3aef48557576e1a85ba7efea8ecb7.jpg"/></a>
    </div>
    <p class="star-rating One">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html" title="Mesaerion: The Best Science Fiction Stories 1800-1849">Mesaerion: The Best Science ...</a></h3>
    <div class="product_price">
    <p class="price_color">£37.59</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/libertarianism-for-beginners_982/index.html"><img alt="Libertarianism for Beginners" class="thumbnail" src="media/cache/0b/bc/0bbcd0a6f4bcd81ccb1049a52736406e.jpg"/></a>
    </div>
    <p class="star-rating Two">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/libertarianism-for-beginners_982/index.html" title="Libertarianism for Beginners">Libertarianism for Beginners</a></h3>
    <div class="product_price">
    <p class="price_color">£51.33</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/its-only-the-himalayas_981/index.html"><img alt="It's Only the Himalayas" class="thumbnail" src="media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg"/></a>
    </div>
    <p class="star-rating Two">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/its-only-the-himalayas_981/index.html" title="It's Only the Himalayas">It's Only the Himalayas</a></h3>
    <div class="product_price">
    <p class="price_color">£45.17</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>
    </ol>
    <div>
    <ul class="pager">
    <li class="current">
                
                    Page 1 of 50
                
                </li>
    <li class="next"><a href="catalogue/page-2.html">next</a></li>
    </ul>
    </div>
    </div>
    </section>
    </div>
    </div><!-- /row -->
    </div><!-- /page_inner -->
    </div><!-- /container-fluid -->
    <footer class="footer container-fluid">
    </footer>
    <!-- jQuery -->
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="static/oscar/js/jquery/jquery-1.9.1.min.js"><\/script>')</script>
    <!-- Twitter Bootstrap -->
    <script src="static/oscar/js/bootstrap3/bootstrap.min.js" type="text/javascript"></script>
    <!-- Oscar -->
    <script charset="utf-8" src="static/oscar/js/oscar/ui.js" type="text/javascript"></script>
    <script charset="utf-8" src="static/oscar/js/bootstrap-datetimepicker/bootstrap-datetimepicker.js" type="text/javascript"></script>
    <script charset="utf-8" src="static/oscar/js/bootstrap-datetimepicker/locales/bootstrap-datetimepicker.all.js" type="text/javascript"></script>
    <script type="text/javascript">
                $(function() {
                    
        
        
        oscar.init();
    
        oscar.search.init();
    
                });
            </script>
    <!-- Version: N/A -->
    </body>
    </html>
    >




```python
type(soup.find_all('li', {'class' : 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}))
```




    bs4.element.ResultSet




```python
# All elements:
all = soup.find_all('li', {'class' : 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
all
```




    [<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>
     </div>
     <p class="star-rating Three">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
     <div class="product_price">
     <p class="price_color">£51.77</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/tipping-the-velvet_999/index.html"><img alt="Tipping the Velvet" class="thumbnail" src="media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg"/></a>
     </div>
     <p class="star-rating One">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/tipping-the-velvet_999/index.html" title="Tipping the Velvet">Tipping the Velvet</a></h3>
     <div class="product_price">
     <p class="price_color">£53.74</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/soumission_998/index.html"><img alt="Soumission" class="thumbnail" src="media/cache/3e/ef/3eef99c9d9adef34639f510662022830.jpg"/></a>
     </div>
     <p class="star-rating One">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/soumission_998/index.html" title="Soumission">Soumission</a></h3>
     <div class="product_price">
     <p class="price_color">£50.10</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/sharp-objects_997/index.html"><img alt="Sharp Objects" class="thumbnail" src="media/cache/32/51/3251cf3a3412f53f339e42cac2134093.jpg"/></a>
     </div>
     <p class="star-rating Four">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/sharp-objects_997/index.html" title="Sharp Objects">Sharp Objects</a></h3>
     <div class="product_price">
     <p class="price_color">£47.82</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/sapiens-a-brief-history-of-humankind_996/index.html"><img alt="Sapiens: A Brief History of Humankind" class="thumbnail" src="media/cache/be/a5/bea5697f2534a2f86a3ef27b5a8c12a6.jpg"/></a>
     </div>
     <p class="star-rating Five">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/sapiens-a-brief-history-of-humankind_996/index.html" title="Sapiens: A Brief History of Humankind">Sapiens: A Brief History ...</a></h3>
     <div class="product_price">
     <p class="price_color">£54.23</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/the-requiem-red_995/index.html"><img alt="The Requiem Red" class="thumbnail" src="media/cache/68/33/68339b4c9bc034267e1da611ab3b34f8.jpg"/></a>
     </div>
     <p class="star-rating One">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/the-requiem-red_995/index.html" title="The Requiem Red">The Requiem Red</a></h3>
     <div class="product_price">
     <p class="price_color">£22.65</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html"><img alt="The Dirty Little Secrets of Getting Your Dream Job" class="thumbnail" src="media/cache/92/27/92274a95b7c251fea59a2b8a78275ab4.jpg"/></a>
     </div>
     <p class="star-rating Four">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html" title="The Dirty Little Secrets of Getting Your Dream Job">The Dirty Little Secrets ...</a></h3>
     <div class="product_price">
     <p class="price_color">£33.34</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html"><img alt="The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull" class="thumbnail" src="media/cache/3d/54/3d54940e57e662c4dd1f3ff00c78cc64.jpg"/></a>
     </div>
     <p class="star-rating Three">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html" title="The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull">The Coming Woman: A ...</a></h3>
     <div class="product_price">
     <p class="price_color">£17.93</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html"><img alt="The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics" class="thumbnail" src="media/cache/66/88/66883b91f6804b2323c8369331cb7dd1.jpg"/></a>
     </div>
     <p class="star-rating Four">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html" title="The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics">The Boys in the ...</a></h3>
     <div class="product_price">
     <p class="price_color">£22.60</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/the-black-maria_991/index.html"><img alt="The Black Maria" class="thumbnail" src="media/cache/58/46/5846057e28022268153beff6d352b06c.jpg"/></a>
     </div>
     <p class="star-rating One">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/the-black-maria_991/index.html" title="The Black Maria">The Black Maria</a></h3>
     <div class="product_price">
     <p class="price_color">£52.15</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html"><img alt="Starving Hearts (Triangular Trade Trilogy, #1)" class="thumbnail" src="media/cache/be/f4/bef44da28c98f905a3ebec0b87be8530.jpg"/></a>
     </div>
     <p class="star-rating Two">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html" title="Starving Hearts (Triangular Trade Trilogy, #1)">Starving Hearts (Triangular Trade ...</a></h3>
     <div class="product_price">
     <p class="price_color">£13.99</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/shakespeares-sonnets_989/index.html"><img alt="Shakespeare's Sonnets" class="thumbnail" src="media/cache/10/48/1048f63d3b5061cd2f424d20b3f9b666.jpg"/></a>
     </div>
     <p class="star-rating Four">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/shakespeares-sonnets_989/index.html" title="Shakespeare's Sonnets">Shakespeare's Sonnets</a></h3>
     <div class="product_price">
     <p class="price_color">£20.66</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/set-me-free_988/index.html"><img alt="Set Me Free" class="thumbnail" src="media/cache/5b/88/5b88c52633f53cacf162c15f4f823153.jpg"/></a>
     </div>
     <p class="star-rating Five">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/set-me-free_988/index.html" title="Set Me Free">Set Me Free</a></h3>
     <div class="product_price">
     <p class="price_color">£17.46</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html"><img alt="Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)" class="thumbnail" src="media/cache/94/b1/94b1b8b244bce9677c2f29ccc890d4d2.jpg"/></a>
     </div>
     <p class="star-rating Five">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html" title="Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)">Scott Pilgrim's Precious Little ...</a></h3>
     <div class="product_price">
     <p class="price_color">£52.29</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/rip-it-up-and-start-again_986/index.html"><img alt="Rip it Up and Start Again" class="thumbnail" src="media/cache/81/c4/81c4a973364e17d01f217e1188253d5e.jpg"/></a>
     </div>
     <p class="star-rating Five">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/rip-it-up-and-start-again_986/index.html" title="Rip it Up and Start Again">Rip it Up and ...</a></h3>
     <div class="product_price">
     <p class="price_color">£35.02</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html"><img alt="Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991" class="thumbnail" src="media/cache/54/60/54607fe8945897cdcced0044103b10b6.jpg"/></a>
     </div>
     <p class="star-rating Three">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html" title="Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991">Our Band Could Be ...</a></h3>
     <div class="product_price">
     <p class="price_color">£57.25</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/olio_984/index.html"><img alt="Olio" class="thumbnail" src="media/cache/55/33/553310a7162dfbc2c6d19a84da0df9e1.jpg"/></a>
     </div>
     <p class="star-rating One">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/olio_984/index.html" title="Olio">Olio</a></h3>
     <div class="product_price">
     <p class="price_color">£23.88</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html"><img alt="Mesaerion: The Best Science Fiction Stories 1800-1849" class="thumbnail" src="media/cache/09/a3/09a3aef48557576e1a85ba7efea8ecb7.jpg"/></a>
     </div>
     <p class="star-rating One">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html" title="Mesaerion: The Best Science Fiction Stories 1800-1849">Mesaerion: The Best Science ...</a></h3>
     <div class="product_price">
     <p class="price_color">£37.59</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/libertarianism-for-beginners_982/index.html"><img alt="Libertarianism for Beginners" class="thumbnail" src="media/cache/0b/bc/0bbcd0a6f4bcd81ccb1049a52736406e.jpg"/></a>
     </div>
     <p class="star-rating Two">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/libertarianism-for-beginners_982/index.html" title="Libertarianism for Beginners">Libertarianism for Beginners</a></h3>
     <div class="product_price">
     <p class="price_color">£51.33</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>,
     <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
     <article class="product_pod">
     <div class="image_container">
     <a href="catalogue/its-only-the-himalayas_981/index.html"><img alt="It's Only the Himalayas" class="thumbnail" src="media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg"/></a>
     </div>
     <p class="star-rating Two">
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     <i class="icon-star"></i>
     </p>
     <h3><a href="catalogue/its-only-the-himalayas_981/index.html" title="It's Only the Himalayas">It's Only the Himalayas</a></h3>
     <div class="product_price">
     <p class="price_color">£45.17</p>
     <p class="instock availability">
     <i class="icon-ok"></i>
         
             In stock
         
     </p>
     <form>
     <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
     </form>
     </div>
     </article>
     </li>]




```python
# To show the first item
f = soup.find_all('li', {'class' : 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})[0]
f
```




    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
    <div class="image_container">
    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>
    </div>
    <p class="star-rating Three">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
    <div class="product_price">
    <p class="price_color">£51.77</p>
    <p class="instock availability">
    <i class="icon-ok"></i>
        
            In stock
        
    </p>
    <form>
    <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
    </form>
    </div>
    </article>
    </li>




```python
f.find_all('a')
```




    [<a href="catalogue/a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>,
     <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>]




```python
f.find('a')
```




    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>




```python
# to get the URL, Title, Price , Instock and the rating

#URL
f.find('a')['href']
```




    'catalogue/a-light-in-the-attic_1000/index.html'




```python
# TO find the title
f.find('h3').find('a')['title']
```




    'A Light in the Attic'




```python
# to find the price
f.find('p', {'class': 'price_color'}).text
```




    '£51.77'




```python
# Find instock

f.find('p',{'class': 'instock availability'}).text
```




    '\n\n    \n        In stock\n    \n'




```python
# TO find the rating

import re
regex  = re.compile('star-rating (.*)')
f.find('p', {'class' : regex})
```




    <p class="star-rating Three">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    </p>




```python
f.find('p',{'class': regex})['class'][-1] 
```




    'Three'




```python
def cleaning(book):
    info = {}
    info['title'] = book.find('h3').find('a')['title']
    info['price'] = book.find('p', {'class': 'price_color'}).text
    if 'In stock' in f.find('p',{'class': 'instock availability'}).text:
        info['instock'] = True
    else:
        info['instock'] = False
    info['stars'] = book.find('p',{'class': regex})['class'][--1]
    info['url'] = 'http://books.toscrape.com/' + book.find('a')['href']
    return info
```


```python
cleaning(f)
```




    {'title': 'A Light in the Attic',
     'price': '£51.77',
     'instock': True,
     'stars': 'Three',
     'url': 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'}




```python
all_dict = [cleaning(book) for book in all]
all_dict
```




    [{'title': 'A Light in the Attic',
      'price': '£51.77',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'},
     {'title': 'Tipping the Velvet',
      'price': '£53.74',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'},
     {'title': 'Soumission',
      'price': '£50.10',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/soumission_998/index.html'},
     {'title': 'Sharp Objects',
      'price': '£47.82',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/catalogue/sharp-objects_997/index.html'},
     {'title': 'Sapiens: A Brief History of Humankind',
      'price': '£54.23',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'},
     {'title': 'The Requiem Red',
      'price': '£22.65',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/the-requiem-red_995/index.html'},
     {'title': 'The Dirty Little Secrets of Getting Your Dream Job',
      'price': '£33.34',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html'},
     {'title': 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull',
      'price': '£17.93',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html'},
     {'title': 'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics',
      'price': '£22.60',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html'},
     {'title': 'The Black Maria',
      'price': '£52.15',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/the-black-maria_991/index.html'},
     {'title': 'Starving Hearts (Triangular Trade Trilogy, #1)',
      'price': '£13.99',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html'},
     {'title': "Shakespeare's Sonnets",
      'price': '£20.66',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html'},
     {'title': 'Set Me Free',
      'price': '£17.46',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/catalogue/set-me-free_988/index.html'},
     {'title': "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)",
      'price': '£52.29',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'},
     {'title': 'Rip it Up and Start Again',
      'price': '£35.02',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html'},
     {'title': 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991',
      'price': '£57.25',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html'},
     {'title': 'Olio',
      'price': '£23.88',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/olio_984/index.html'},
     {'title': 'Mesaerion: The Best Science Fiction Stories 1800-1849',
      'price': '£37.59',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html'},
     {'title': 'Libertarianism for Beginners',
      'price': '£51.33',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html'},
     {'title': "It's Only the Himalayas",
      'price': '£45.17',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'}]




```python

pd.DataFrame(all_dict)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>price</th>
      <th>instock</th>
      <th>stars</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A Light in the Attic</td>
      <td>£51.77</td>
      <td>True</td>
      <td>Three</td>
      <td>http://books.toscrape.com/catalogue/a-light-in...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tipping the Velvet</td>
      <td>£53.74</td>
      <td>True</td>
      <td>One</td>
      <td>http://books.toscrape.com/catalogue/tipping-th...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Soumission</td>
      <td>£50.10</td>
      <td>True</td>
      <td>One</td>
      <td>http://books.toscrape.com/catalogue/soumission...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sharp Objects</td>
      <td>£47.82</td>
      <td>True</td>
      <td>Four</td>
      <td>http://books.toscrape.com/catalogue/sharp-obje...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sapiens: A Brief History of Humankind</td>
      <td>£54.23</td>
      <td>True</td>
      <td>Five</td>
      <td>http://books.toscrape.com/catalogue/sapiens-a-...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>The Requiem Red</td>
      <td>£22.65</td>
      <td>True</td>
      <td>One</td>
      <td>http://books.toscrape.com/catalogue/the-requie...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>The Dirty Little Secrets of Getting Your Dream...</td>
      <td>£33.34</td>
      <td>True</td>
      <td>Four</td>
      <td>http://books.toscrape.com/catalogue/the-dirty-...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>The Coming Woman: A Novel Based on the Life of...</td>
      <td>£17.93</td>
      <td>True</td>
      <td>Three</td>
      <td>http://books.toscrape.com/catalogue/the-coming...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>The Boys in the Boat: Nine Americans and Their...</td>
      <td>£22.60</td>
      <td>True</td>
      <td>Four</td>
      <td>http://books.toscrape.com/catalogue/the-boys-i...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>The Black Maria</td>
      <td>£52.15</td>
      <td>True</td>
      <td>One</td>
      <td>http://books.toscrape.com/catalogue/the-black-...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Starving Hearts (Triangular Trade Trilogy, #1)</td>
      <td>£13.99</td>
      <td>True</td>
      <td>Two</td>
      <td>http://books.toscrape.com/catalogue/starving-h...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shakespeare's Sonnets</td>
      <td>£20.66</td>
      <td>True</td>
      <td>Four</td>
      <td>http://books.toscrape.com/catalogue/shakespear...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Set Me Free</td>
      <td>£17.46</td>
      <td>True</td>
      <td>Five</td>
      <td>http://books.toscrape.com/catalogue/set-me-fre...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Scott Pilgrim's Precious Little Life (Scott Pi...</td>
      <td>£52.29</td>
      <td>True</td>
      <td>Five</td>
      <td>http://books.toscrape.com/catalogue/scott-pilg...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Rip it Up and Start Again</td>
      <td>£35.02</td>
      <td>True</td>
      <td>Five</td>
      <td>http://books.toscrape.com/catalogue/rip-it-up-...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Our Band Could Be Your Life: Scenes from the A...</td>
      <td>£57.25</td>
      <td>True</td>
      <td>Three</td>
      <td>http://books.toscrape.com/catalogue/our-band-c...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Olio</td>
      <td>£23.88</td>
      <td>True</td>
      <td>One</td>
      <td>http://books.toscrape.com/catalogue/olio_984/i...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Mesaerion: The Best Science Fiction Stories 18...</td>
      <td>£37.59</td>
      <td>True</td>
      <td>One</td>
      <td>http://books.toscrape.com/catalogue/mesaerion-...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Libertarianism for Beginners</td>
      <td>£51.33</td>
      <td>True</td>
      <td>Two</td>
      <td>http://books.toscrape.com/catalogue/libertaria...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>It's Only the Himalayas</td>
      <td>£45.17</td>
      <td>True</td>
      <td>Two</td>
      <td>http://books.toscrape.com/catalogue/its-only-t...</td>
    </tr>
  </tbody>
</table>
</div>



# Scraping multiple pages (Pagination!)


```python
url = 'https://books.toscrape.com/catalogue/page-2.html'

```


```python
# Urls for all the other pages
urls = ['https://books.toscrape.com/catalogue/page-{}.html'.format(i) for i in range (1,51)]
urls
```




    ['https://books.toscrape.com/catalogue/page-1.html',
     'https://books.toscrape.com/catalogue/page-2.html',
     'https://books.toscrape.com/catalogue/page-3.html',
     'https://books.toscrape.com/catalogue/page-4.html',
     'https://books.toscrape.com/catalogue/page-5.html',
     'https://books.toscrape.com/catalogue/page-6.html',
     'https://books.toscrape.com/catalogue/page-7.html',
     'https://books.toscrape.com/catalogue/page-8.html',
     'https://books.toscrape.com/catalogue/page-9.html',
     'https://books.toscrape.com/catalogue/page-10.html',
     'https://books.toscrape.com/catalogue/page-11.html',
     'https://books.toscrape.com/catalogue/page-12.html',
     'https://books.toscrape.com/catalogue/page-13.html',
     'https://books.toscrape.com/catalogue/page-14.html',
     'https://books.toscrape.com/catalogue/page-15.html',
     'https://books.toscrape.com/catalogue/page-16.html',
     'https://books.toscrape.com/catalogue/page-17.html',
     'https://books.toscrape.com/catalogue/page-18.html',
     'https://books.toscrape.com/catalogue/page-19.html',
     'https://books.toscrape.com/catalogue/page-20.html',
     'https://books.toscrape.com/catalogue/page-21.html',
     'https://books.toscrape.com/catalogue/page-22.html',
     'https://books.toscrape.com/catalogue/page-23.html',
     'https://books.toscrape.com/catalogue/page-24.html',
     'https://books.toscrape.com/catalogue/page-25.html',
     'https://books.toscrape.com/catalogue/page-26.html',
     'https://books.toscrape.com/catalogue/page-27.html',
     'https://books.toscrape.com/catalogue/page-28.html',
     'https://books.toscrape.com/catalogue/page-29.html',
     'https://books.toscrape.com/catalogue/page-30.html',
     'https://books.toscrape.com/catalogue/page-31.html',
     'https://books.toscrape.com/catalogue/page-32.html',
     'https://books.toscrape.com/catalogue/page-33.html',
     'https://books.toscrape.com/catalogue/page-34.html',
     'https://books.toscrape.com/catalogue/page-35.html',
     'https://books.toscrape.com/catalogue/page-36.html',
     'https://books.toscrape.com/catalogue/page-37.html',
     'https://books.toscrape.com/catalogue/page-38.html',
     'https://books.toscrape.com/catalogue/page-39.html',
     'https://books.toscrape.com/catalogue/page-40.html',
     'https://books.toscrape.com/catalogue/page-41.html',
     'https://books.toscrape.com/catalogue/page-42.html',
     'https://books.toscrape.com/catalogue/page-43.html',
     'https://books.toscrape.com/catalogue/page-44.html',
     'https://books.toscrape.com/catalogue/page-45.html',
     'https://books.toscrape.com/catalogue/page-46.html',
     'https://books.toscrape.com/catalogue/page-47.html',
     'https://books.toscrape.com/catalogue/page-48.html',
     'https://books.toscrape.com/catalogue/page-49.html',
     'https://books.toscrape.com/catalogue/page-50.html']




```python
# To get the 20 books for each page

def get_20_books(url):
    html_page = requests.get(url)
    soup = bs(html_page.content, 'html.parser')
    
    raw = soup.find_all ('li' ,{'class' : 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
    to_dicts = [cleaning(book) for book in raw]
    
    return to_dicts
    

```


```python
get_20_books('https://books.toscrape.com/')

```




    [{'title': 'A Light in the Attic',
      'price': '£51.77',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'},
     {'title': 'Tipping the Velvet',
      'price': '£53.74',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'},
     {'title': 'Soumission',
      'price': '£50.10',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/soumission_998/index.html'},
     {'title': 'Sharp Objects',
      'price': '£47.82',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/catalogue/sharp-objects_997/index.html'},
     {'title': 'Sapiens: A Brief History of Humankind',
      'price': '£54.23',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'},
     {'title': 'The Requiem Red',
      'price': '£22.65',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/the-requiem-red_995/index.html'},
     {'title': 'The Dirty Little Secrets of Getting Your Dream Job',
      'price': '£33.34',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html'},
     {'title': 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull',
      'price': '£17.93',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html'},
     {'title': 'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics',
      'price': '£22.60',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html'},
     {'title': 'The Black Maria',
      'price': '£52.15',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/the-black-maria_991/index.html'},
     {'title': 'Starving Hearts (Triangular Trade Trilogy, #1)',
      'price': '£13.99',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html'},
     {'title': "Shakespeare's Sonnets",
      'price': '£20.66',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html'},
     {'title': 'Set Me Free',
      'price': '£17.46',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/catalogue/set-me-free_988/index.html'},
     {'title': "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)",
      'price': '£52.29',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'},
     {'title': 'Rip it Up and Start Again',
      'price': '£35.02',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html'},
     {'title': 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991',
      'price': '£57.25',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html'},
     {'title': 'Olio',
      'price': '£23.88',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/olio_984/index.html'},
     {'title': 'Mesaerion: The Best Science Fiction Stories 1800-1849',
      'price': '£37.59',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html'},
     {'title': 'Libertarianism for Beginners',
      'price': '£51.33',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html'},
     {'title': "It's Only the Himalayas",
      'price': '£45.17',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'}]




```python
all_dicts = []

for url in urls:
    all_dicts.extend(get_20_books(url))
    
all_dicts    
```




    [{'title': 'A Light in the Attic',
      'price': '£51.77',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/a-light-in-the-attic_1000/index.html'},
     {'title': 'Tipping the Velvet',
      'price': '£53.74',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/tipping-the-velvet_999/index.html'},
     {'title': 'Soumission',
      'price': '£50.10',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/soumission_998/index.html'},
     {'title': 'Sharp Objects',
      'price': '£47.82',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/sharp-objects_997/index.html'},
     {'title': 'Sapiens: A Brief History of Humankind',
      'price': '£54.23',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/sapiens-a-brief-history-of-humankind_996/index.html'},
     {'title': 'The Requiem Red',
      'price': '£22.65',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-requiem-red_995/index.html'},
     {'title': 'The Dirty Little Secrets of Getting Your Dream Job',
      'price': '£33.34',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html'},
     {'title': 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull',
      'price': '£17.93',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html'},
     {'title': 'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics',
      'price': '£22.60',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html'},
     {'title': 'The Black Maria',
      'price': '£52.15',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-black-maria_991/index.html'},
     {'title': 'Starving Hearts (Triangular Trade Trilogy, #1)',
      'price': '£13.99',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/starving-hearts-triangular-trade-trilogy-1_990/index.html'},
     {'title': "Shakespeare's Sonnets",
      'price': '£20.66',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/shakespeares-sonnets_989/index.html'},
     {'title': 'Set Me Free',
      'price': '£17.46',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/set-me-free_988/index.html'},
     {'title': "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)",
      'price': '£52.29',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'},
     {'title': 'Rip it Up and Start Again',
      'price': '£35.02',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/rip-it-up-and-start-again_986/index.html'},
     {'title': 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991',
      'price': '£57.25',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html'},
     {'title': 'Olio',
      'price': '£23.88',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/olio_984/index.html'},
     {'title': 'Mesaerion: The Best Science Fiction Stories 1800-1849',
      'price': '£37.59',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html'},
     {'title': 'Libertarianism for Beginners',
      'price': '£51.33',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/libertarianism-for-beginners_982/index.html'},
     {'title': "It's Only the Himalayas",
      'price': '£45.17',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/its-only-the-himalayas_981/index.html'},
     {'title': 'In Her Wake',
      'price': '£12.84',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/in-her-wake_980/index.html'},
     {'title': 'How Music Works',
      'price': '£37.32',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/how-music-works_979/index.html'},
     {'title': 'Foolproof Preserving: A Guide to Small Batch Jams, Jellies, Pickles, Condiments, and More: A Foolproof Guide to Making Small Batch Jams, Jellies, Pickles, Condiments, and More',
      'price': '£30.52',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/foolproof-preserving-a-guide-to-small-batch-jams-jellies-pickles-condiments-and-more-a-foolproof-guide-to-making-small-batch-jams-jellies-pickles-condiments-and-more_978/index.html'},
     {'title': 'Chase Me (Paris Nights #2)',
      'price': '£25.27',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/chase-me-paris-nights-2_977/index.html'},
     {'title': 'Black Dust',
      'price': '£34.53',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/black-dust_976/index.html'},
     {'title': 'Birdsong: A Story in Pictures',
      'price': '£54.64',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/birdsong-a-story-in-pictures_975/index.html'},
     {'title': "America's Cradle of Quarterbacks: Western Pennsylvania's Football Factory from Johnny Unitas to Joe Montana",
      'price': '£22.50',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/americas-cradle-of-quarterbacks-western-pennsylvanias-football-factory-from-johnny-unitas-to-joe-montana_974/index.html'},
     {'title': 'Aladdin and His Wonderful Lamp',
      'price': '£53.13',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/aladdin-and-his-wonderful-lamp_973/index.html'},
     {'title': 'Worlds Elsewhere: Journeys Around Shakespeare’s Globe',
      'price': '£40.30',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html'},
     {'title': 'Wall and Piece',
      'price': '£44.18',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/wall-and-piece_971/index.html'},
     {'title': 'The Four Agreements: A Practical Guide to Personal Freedom',
      'price': '£17.66',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-four-agreements-a-practical-guide-to-personal-freedom_970/index.html'},
     {'title': 'The Five Love Languages: How to Express Heartfelt Commitment to Your Mate',
      'price': '£31.05',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-five-love-languages-how-to-express-heartfelt-commitment-to-your-mate_969/index.html'},
     {'title': 'The Elephant Tree',
      'price': '£23.82',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-elephant-tree_968/index.html'},
     {'title': 'The Bear and the Piano',
      'price': '£36.89',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-bear-and-the-piano_967/index.html'},
     {'title': "Sophie's World",
      'price': '£15.94',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/sophies-world_966/index.html'},
     {'title': 'Penny Maybe',
      'price': '£33.29',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/penny-maybe_965/index.html'},
     {'title': 'Maude (1883-1993):She Grew Up with the country',
      'price': '£18.02',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/maude-1883-1993she-grew-up-with-the-country_964/index.html'},
     {'title': 'In a Dark, Dark Wood',
      'price': '£19.63',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/in-a-dark-dark-wood_963/index.html'},
     {'title': 'Behind Closed Doors',
      'price': '£52.22',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/behind-closed-doors_962/index.html'},
     {'title': "You can't bury them all: Poems",
      'price': '£33.63',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/you-cant-bury-them-all-poems_961/index.html'},
     {'title': 'Slow States of Collapse: Poems',
      'price': '£57.31',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/slow-states-of-collapse-poems_960/index.html'},
     {'title': 'Reasons to Stay Alive',
      'price': '£26.41',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/reasons-to-stay-alive_959/index.html'},
     {'title': 'Private Paris (Private #10)',
      'price': '£47.61',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/private-paris-private-10_958/index.html'},
     {'title': '#HigherSelfie: Wake Up Your Life. Free Your Soul. Find Your Tribe.',
      'price': '£23.11',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/higherselfie-wake-up-your-life-free-your-soul-find-your-tribe_957/index.html'},
     {'title': 'Without Borders (Wanderlove #1)',
      'price': '£45.07',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/without-borders-wanderlove-1_956/index.html'},
     {'title': 'When We Collided',
      'price': '£31.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/when-we-collided_955/index.html'},
     {'title': 'We Love You, Charlie Freeman',
      'price': '£50.27',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/we-love-you-charlie-freeman_954/index.html'},
     {'title': 'Untitled Collection: Sabbath Poems 2014',
      'price': '£14.27',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/untitled-collection-sabbath-poems-2014_953/index.html'},
     {'title': 'Unseen City: The Majesty of Pigeons, the Discreet Charm of Snails & Other Wonders of the Urban Wilderness',
      'price': '£44.18',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/unseen-city-the-majesty-of-pigeons-the-discreet-charm-of-snails-other-wonders-of-the-urban-wilderness_952/index.html'},
     {'title': 'Unicorn Tracks',
      'price': '£18.78',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/unicorn-tracks_951/index.html'},
     {'title': 'Unbound: How Eight Technologies Made Us Human, Transformed Society, and Brought Our World to the Brink',
      'price': '£25.52',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/unbound-how-eight-technologies-made-us-human-transformed-society-and-brought-our-world-to-the-brink_950/index.html'},
     {'title': 'Tsubasa: WoRLD CHRoNiCLE 2 (Tsubasa WoRLD CHRoNiCLE #2)',
      'price': '£16.28',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/tsubasa-world-chronicle-2-tsubasa-world-chronicle-2_949/index.html'},
     {'title': 'Throwing Rocks at the Google Bus: How Growth Became the Enemy of Prosperity',
      'price': '£31.12',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/throwing-rocks-at-the-google-bus-how-growth-became-the-enemy-of-prosperity_948/index.html'},
     {'title': 'This One Summer',
      'price': '£19.49',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/this-one-summer_947/index.html'},
     {'title': 'Thirst',
      'price': '£17.27',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/thirst_946/index.html'},
     {'title': 'The Torch Is Passed: A Harding Family Story',
      'price': '£19.09',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-torch-is-passed-a-harding-family-story_945/index.html'},
     {'title': 'The Secret of Dreadwillow Carse',
      'price': '£56.13',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-secret-of-dreadwillow-carse_944/index.html'},
     {'title': 'The Pioneer Woman Cooks: Dinnertime: Comfort Classics, Freezer Food, 16-Minute Meals, and Other Delicious Ways to Solve Supper!',
      'price': '£56.41',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-pioneer-woman-cooks-dinnertime-comfort-classics-freezer-food-16-minute-meals-and-other-delicious-ways-to-solve-supper_943/index.html'},
     {'title': 'The Past Never Ends',
      'price': '£56.50',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-past-never-ends_942/index.html'},
     {'title': 'The Natural History of Us (The Fine Art of Pretending #2)',
      'price': '£45.22',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-natural-history-of-us-the-fine-art-of-pretending-2_941/index.html'},
     {'title': 'The Nameless City (The Nameless City #1)',
      'price': '£38.16',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-nameless-city-the-nameless-city-1_940/index.html'},
     {'title': 'The Murder That Never Was (Forensic Instincts #5)',
      'price': '£54.11',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-murder-that-never-was-forensic-instincts-5_939/index.html'},
     {'title': "The Most Perfect Thing: Inside (and Outside) a Bird's Egg",
      'price': '£42.96',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-most-perfect-thing-inside-and-outside-a-birds-egg_938/index.html'},
     {'title': 'The Mindfulness and Acceptance Workbook for Anxiety: A Guide to Breaking Free from Anxiety, Phobias, and Worry Using Acceptance and Commitment Therapy',
      'price': '£23.89',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-mindfulness-and-acceptance-workbook-for-anxiety-a-guide-to-breaking-free-from-anxiety-phobias-and-worry-using-acceptance-and-commitment-therapy_937/index.html'},
     {'title': 'The Life-Changing Magic of Tidying Up: The Japanese Art of Decluttering and Organizing',
      'price': '£16.77',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-life-changing-magic-of-tidying-up-the-japanese-art-of-decluttering-and-organizing_936/index.html'},
     {'title': 'The Inefficiency Assassin: Time Management Tactics for Working Smarter, Not Longer',
      'price': '£20.59',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-inefficiency-assassin-time-management-tactics-for-working-smarter-not-longer_935/index.html'},
     {'title': 'The Gutsy Girl: Escapades for Your Life of Epic Adventure',
      'price': '£37.13',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-gutsy-girl-escapades-for-your-life-of-epic-adventure_934/index.html'},
     {'title': 'The Electric Pencil: Drawings from Inside State Hospital No. 3',
      'price': '£56.06',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-electric-pencil-drawings-from-inside-state-hospital-no-3_933/index.html'},
     {'title': 'The Death of Humanity: and the Case for Life',
      'price': '£58.11',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-death-of-humanity-and-the-case-for-life_932/index.html'},
     {'title': 'The Bulletproof Diet: Lose up to a Pound a Day, Reclaim Energy and Focus, Upgrade Your Life',
      'price': '£49.05',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-bulletproof-diet-lose-up-to-a-pound-a-day-reclaim-energy-and-focus-upgrade-your-life_931/index.html'},
     {'title': 'The Art Forger',
      'price': '£40.76',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-art-forger_930/index.html'},
     {'title': 'The Age of Genius: The Seventeenth Century and the Birth of the Modern Mind',
      'price': '£19.73',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-age-of-genius-the-seventeenth-century-and-the-birth-of-the-modern-mind_929/index.html'},
     {'title': "The Activist's Tao Te Ching: Ancient Advice for a Modern Revolution",
      'price': '£32.24',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-activists-tao-te-ching-ancient-advice-for-a-modern-revolution_928/index.html'},
     {'title': 'Spark Joy: An Illustrated Master Class on the Art of Organizing and Tidying Up',
      'price': '£41.83',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/spark-joy-an-illustrated-master-class-on-the-art-of-organizing-and-tidying-up_927/index.html'},
     {'title': 'Soul Reader',
      'price': '£39.58',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/soul-reader_926/index.html'},
     {'title': 'Security',
      'price': '£39.25',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/security_925/index.html'},
     {'title': 'Saga, Volume 6 (Saga (Collected Editions) #6)',
      'price': '£25.02',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/saga-volume-6-saga-collected-editions-6_924/index.html'},
     {'title': 'Saga, Volume 5 (Saga (Collected Editions) #5)',
      'price': '£51.04',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/saga-volume-5-saga-collected-editions-5_923/index.html'},
     {'title': 'Reskilling America: Learning to Labor in the Twenty-First Century',
      'price': '£19.83',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/reskilling-america-learning-to-labor-in-the-twenty-first-century_922/index.html'},
     {'title': 'Rat Queens, Vol. 3: Demons (Rat Queens (Collected Editions) #11-15)',
      'price': '£50.40',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/rat-queens-vol-3-demons-rat-queens-collected-editions-11-15_921/index.html'},
     {'title': 'Princess Jellyfish 2-in-1 Omnibus, Vol. 01 (Princess Jellyfish 2-in-1 Omnibus #1)',
      'price': '£13.61',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/princess-jellyfish-2-in-1-omnibus-vol-01-princess-jellyfish-2-in-1-omnibus-1_920/index.html'},
     {'title': 'Princess Between Worlds (Wide-Awake Princess #5)',
      'price': '£13.34',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/princess-between-worlds-wide-awake-princess-5_919/index.html'},
     {'title': 'Pop Gun War, Volume 1: Gift',
      'price': '£18.97',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/pop-gun-war-volume-1-gift_918/index.html'},
     {'title': 'Political Suicide: Missteps, Peccadilloes, Bad Calls, Backroom Hijinx, Sordid Pasts, Rotten Breaks, and Just Plain Dumb Mistakes in the Annals of American Politics',
      'price': '£36.28',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/political-suicide-missteps-peccadilloes-bad-calls-backroom-hijinx-sordid-pasts-rotten-breaks-and-just-plain-dumb-mistakes-in-the-annals-of-american-politics_917/index.html'},
     {'title': 'Patience',
      'price': '£10.16',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/patience_916/index.html'},
     {'title': 'Outcast, Vol. 1: A Darkness Surrounds Him (Outcast #1)',
      'price': '£15.44',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/outcast-vol-1-a-darkness-surrounds-him-outcast-1_915/index.html'},
     {'title': 'orange: The Complete Collection 1 (orange: The Complete Collection #1)',
      'price': '£48.41',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/orange-the-complete-collection-1-orange-the-complete-collection-1_914/index.html'},
     {'title': 'Online Marketing for Busy Authors: A Step-By-Step Guide',
      'price': '£46.35',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/online-marketing-for-busy-authors-a-step-by-step-guide_913/index.html'},
     {'title': 'On a Midnight Clear',
      'price': '£14.07',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/on-a-midnight-clear_912/index.html'},
     {'title': 'Obsidian (Lux #1)',
      'price': '£14.86',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/obsidian-lux-1_911/index.html'},
     {'title': 'My Paris Kitchen: Recipes and Stories',
      'price': '£33.37',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/my-paris-kitchen-recipes-and-stories_910/index.html'},
     {'title': 'Masks and Shadows',
      'price': '£56.40',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/masks-and-shadows_909/index.html'},
     {'title': 'Mama Tried: Traditional Italian Cooking for the Screwed, Crude, Vegan, and Tattooed',
      'price': '£14.02',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/mama-tried-traditional-italian-cooking-for-the-screwed-crude-vegan-and-tattooed_908/index.html'},
     {'title': 'Lumberjanes, Vol. 2: Friendship to the Max (Lumberjanes #5-8)',
      'price': '£46.91',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/lumberjanes-vol-2-friendship-to-the-max-lumberjanes-5-8_907/index.html'},
     {'title': 'Lumberjanes, Vol. 1: Beware the Kitten Holy (Lumberjanes #1-4)',
      'price': '£45.61',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/lumberjanes-vol-1-beware-the-kitten-holy-lumberjanes-1-4_906/index.html'},
     {'title': 'Lumberjanes Vol. 3: A Terrible Plan (Lumberjanes #9-12)',
      'price': '£19.92',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/lumberjanes-vol-3-a-terrible-plan-lumberjanes-9-12_905/index.html'},
     {'title': 'Layered: Baking, Building, and Styling Spectacular Cakes',
      'price': '£40.11',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/layered-baking-building-and-styling-spectacular-cakes_904/index.html'},
     {'title': 'Judo: Seven Steps to Black Belt (an Introductory Guide for Beginners)',
      'price': '£53.90',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/judo-seven-steps-to-black-belt-an-introductory-guide-for-beginners_903/index.html'},
     {'title': 'Join',
      'price': '£35.67',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/join_902/index.html'},
     {'title': 'In the Country We Love: My Family Divided',
      'price': '£22.00',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/in-the-country-we-love-my-family-divided_901/index.html'},
     {'title': 'Immunity: How Elie Metchnikoff Changed the Course of Modern Medicine',
      'price': '£57.36',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/immunity-how-elie-metchnikoff-changed-the-course-of-modern-medicine_900/index.html'},
     {'title': 'I Hate Fairyland, Vol. 1: Madly Ever After (I Hate Fairyland (Compilations) #1-5)',
      'price': '£29.17',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/i-hate-fairyland-vol-1-madly-ever-after-i-hate-fairyland-compilations-1-5_899/index.html'},
     {'title': 'I am a Hero Omnibus Volume 1',
      'price': '£54.63',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/i-am-a-hero-omnibus-volume-1_898/index.html'},
     {'title': 'How to Be Miserable: 40 Strategies You Already Use',
      'price': '£46.03',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/how-to-be-miserable-40-strategies-you-already-use_897/index.html'},
     {'title': 'Her Backup Boyfriend (The Sorensen Family #1)',
      'price': '£33.97',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/her-backup-boyfriend-the-sorensen-family-1_896/index.html'},
     {'title': 'Giant Days, Vol. 2 (Giant Days #5-8)',
      'price': '£22.11',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/giant-days-vol-2-giant-days-5-8_895/index.html'},
     {'title': 'Forever and Forever: The Courtship of Henry Longfellow and Fanny Appleton',
      'price': '£29.69',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/forever-and-forever-the-courtship-of-henry-longfellow-and-fanny-appleton_894/index.html'},
     {'title': 'First and First (Five Boroughs #3)',
      'price': '£15.97',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/first-and-first-five-boroughs-3_893/index.html'},
     {'title': 'Fifty Shades Darker (Fifty Shades #2)',
      'price': '£21.96',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/fifty-shades-darker-fifty-shades-2_892/index.html'},
     {'title': 'Everydata: The Misinformation Hidden in the Little Data You Consume Every Day',
      'price': '£54.35',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/everydata-the-misinformation-hidden-in-the-little-data-you-consume-every-day_891/index.html'},
     {'title': "Don't Be a Jerk: And Other Practical Advice from Dogen, Japan's Greatest Zen Master",
      'price': '£37.97',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/dont-be-a-jerk-and-other-practical-advice-from-dogen-japans-greatest-zen-master_890/index.html'},
     {'title': 'Danganronpa Volume 1',
      'price': '£51.99',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/danganronpa-volume-1_889/index.html'},
     {'title': 'Crown of Midnight (Throne of Glass #2)',
      'price': '£43.29',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/crown-of-midnight-throne-of-glass-2_888/index.html'},
     {'title': 'Codename Baboushka, Volume 1: The Conclave of Death',
      'price': '£36.72',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/codename-baboushka-volume-1-the-conclave-of-death_887/index.html'},
     {'title': 'Camp Midnight',
      'price': '£17.08',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/camp-midnight_886/index.html'},
     {'title': 'Call the Nurse: True Stories of a Country Nurse on a Scottish Isle',
      'price': '£29.14',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/call-the-nurse-true-stories-of-a-country-nurse-on-a-scottish-isle_885/index.html'},
     {'title': 'Burning',
      'price': '£28.81',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/burning_884/index.html'},
     {'title': 'Bossypants',
      'price': '£49.46',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/bossypants_883/index.html'},
     {'title': 'Bitch Planet, Vol. 1: Extraordinary Machine (Bitch Planet (Collected Editions))',
      'price': '£37.92',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/bitch-planet-vol-1-extraordinary-machine-bitch-planet-collected-editions_882/index.html'},
     {'title': 'Avatar: The Last Airbender: Smoke and Shadow, Part 3 (Smoke and Shadow #3)',
      'price': '£28.09',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/avatar-the-last-airbender-smoke-and-shadow-part-3-smoke-and-shadow-3_881/index.html'},
     {'title': 'Algorithms to Live By: The Computer Science of Human Decisions',
      'price': '£30.81',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/algorithms-to-live-by-the-computer-science-of-human-decisions_880/index.html'},
     {'title': 'A World of Flavor: Your Gluten Free Passport',
      'price': '£42.95',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/a-world-of-flavor-your-gluten-free-passport_879/index.html'},
     {'title': 'A Piece of Sky, a Grain of Rice: A Memoir in Four Meditations',
      'price': '£56.76',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/a-piece-of-sky-a-grain-of-rice-a-memoir-in-four-meditations_878/index.html'},
     {'title': 'A Murder in Time',
      'price': '£16.64',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/a-murder-in-time_877/index.html'},
     {'title': 'A Flight of Arrows (The Pathfinders #2)',
      'price': '£55.53',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/a-flight-of-arrows-the-pathfinders-2_876/index.html'},
     {'title': 'A Fierce and Subtle Poison',
      'price': '£28.13',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/a-fierce-and-subtle-poison_875/index.html'},
     {'title': 'A Court of Thorns and Roses (A Court of Thorns and Roses #1)',
      'price': '£52.37',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/a-court-of-thorns-and-roses-a-court-of-thorns-and-roses-1_874/index.html'},
     {'title': '(Un)Qualified: How God Uses Broken People to Do Big Things',
      'price': '£54.00',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/unqualified-how-god-uses-broken-people-to-do-big-things_873/index.html'},
     {'title': 'You Are What You Love: The Spiritual Power of Habit',
      'price': '£21.87',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/you-are-what-you-love-the-spiritual-power-of-habit_872/index.html'},
     {'title': "William Shakespeare's Star Wars: Verily, A New Hope (William Shakespeare's Star Wars #4)",
      'price': '£43.30',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/william-shakespeares-star-wars-verily-a-new-hope-william-shakespeares-star-wars-4_871/index.html'},
     {'title': 'Tuesday Nights in 1980',
      'price': '£21.04',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/tuesday-nights-in-1980_870/index.html'},
     {'title': 'Tracing Numbers on a Train',
      'price': '£41.60',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/tracing-numbers-on-a-train_869/index.html'},
     {'title': 'Throne of Glass (Throne of Glass #1)',
      'price': '£35.07',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/throne-of-glass-throne-of-glass-1_868/index.html'},
     {'title': 'Thomas Jefferson and the Tripoli Pirates: The Forgotten War That Changed American History',
      'price': '£59.64',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/thomas-jefferson-and-the-tripoli-pirates-the-forgotten-war-that-changed-american-history_867/index.html'},
     {'title': 'Thirteen Reasons Why',
      'price': '£52.72',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/thirteen-reasons-why_866/index.html'},
     {'title': 'The White Cat and the Monk: A Retelling of the Poem “Pangur Bán”',
      'price': '£58.08',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-white-cat-and-the-monk-a-retelling-of-the-poem-pangur-ban_865/index.html'},
     {'title': 'The Wedding Dress',
      'price': '£24.12',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-wedding-dress_864/index.html'},
     {'title': 'The Vacationers',
      'price': '£42.15',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-vacationers_863/index.html'},
     {'title': 'The Third Wave: An Entrepreneur’s Vision of the Future',
      'price': '£12.61',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-third-wave-an-entrepreneurs-vision-of-the-future_862/index.html'},
     {'title': 'The Stranger',
      'price': '£17.44',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-stranger_861/index.html'},
     {'title': 'The Shadow Hero (The Shadow Hero)',
      'price': '£33.14',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-shadow-hero-the-shadow-hero_860/index.html'},
     {'title': 'The Secret (The Secret #1)',
      'price': '£27.37',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-secret-the-secret-1_859/index.html'},
     {'title': 'The Regional Office Is Under Attack!',
      'price': '£51.36',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-regional-office-is-under-attack_858/index.html'},
     {'title': 'The Psychopath Test: A Journey Through the Madness Industry',
      'price': '£36.00',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-psychopath-test-a-journey-through-the-madness-industry_857/index.html'},
     {'title': 'The Project',
      'price': '£10.65',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-project_856/index.html'},
     {'title': 'The Power of Now: A Guide to Spiritual Enlightenment',
      'price': '£43.54',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-power-of-now-a-guide-to-spiritual-enlightenment_855/index.html'},
     {'title': "The Omnivore's Dilemma: A Natural History of Four Meals",
      'price': '£38.21',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-omnivores-dilemma-a-natural-history-of-four-meals_854/index.html'},
     {'title': 'The Nerdy Nummies Cookbook: Sweet Treats for the Geek in All of Us',
      'price': '£37.34',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-nerdy-nummies-cookbook-sweet-treats-for-the-geek-in-all-of-us_853/index.html'},
     {'title': 'The Murder of Roger Ackroyd (Hercule Poirot #4)',
      'price': '£44.10',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-murder-of-roger-ackroyd-hercule-poirot-4_852/index.html'},
     {'title': 'The Mistake (Off-Campus #2)',
      'price': '£43.29',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-mistake-off-campus-2_851/index.html'},
     {'title': "The Matchmaker's Playbook (Wingmen Inc. #1)",
      'price': '£55.85',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-matchmakers-playbook-wingmen-inc-1_850/index.html'},
     {'title': 'The Love and Lemons Cookbook: An Apple-to-Zucchini Celebration of Impromptu Cooking',
      'price': '£37.60',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-love-and-lemons-cookbook-an-apple-to-zucchini-celebration-of-impromptu-cooking_849/index.html'},
     {'title': 'The Long Shadow of Small Ghosts: Murder and Memory in an American City',
      'price': '£10.97',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-long-shadow-of-small-ghosts-murder-and-memory-in-an-american-city_848/index.html'},
     {'title': 'The Kite Runner',
      'price': '£41.82',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-kite-runner_847/index.html'},
     {'title': 'The House by the Lake',
      'price': '£36.95',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-house-by-the-lake_846/index.html'},
     {'title': 'The Glittering Court (The Glittering Court #1)',
      'price': '£44.28',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-glittering-court-the-glittering-court-1_845/index.html'},
     {'title': 'The Girl on the Train',
      'price': '£55.02',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-girl-on-the-train_844/index.html'},
     {'title': 'The Genius of Birds',
      'price': '£17.24',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-genius-of-birds_843/index.html'},
     {'title': 'The Emerald Mystery',
      'price': '£23.15',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-emerald-mystery_842/index.html'},
     {'title': 'The Cookies & Cups Cookbook: 125+ sweet & savory recipes reminding you to Always Eat Dessert First',
      'price': '£41.25',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-cookies-cups-cookbook-125-sweet-savory-recipes-reminding-you-to-always-eat-dessert-first_841/index.html'},
     {'title': "The Bridge to Consciousness: I'm Writing the Bridge Between Science and Our Old and New Beliefs.",
      'price': '£32.00',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-bridge-to-consciousness-im-writing-the-bridge-between-science-and-our-old-and-new-beliefs_840/index.html'},
     {'title': "The Artist's Way: A Spiritual Path to Higher Creativity",
      'price': '£38.49',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-artists-way-a-spiritual-path-to-higher-creativity_839/index.html'},
     {'title': 'The Art of War',
      'price': '£33.34',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-art-of-war_838/index.html'},
     {'title': 'The Argonauts',
      'price': '£10.93',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-argonauts_837/index.html'},
     {'title': 'The 10% Entrepreneur: Live Your Startup Dream Without Quitting Your Day Job',
      'price': '£27.55',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-10-entrepreneur-live-your-startup-dream-without-quitting-your-day-job_836/index.html'},
     {'title': 'Suddenly in Love (Lake Haven #1)',
      'price': '£55.99',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/suddenly-in-love-lake-haven-1_835/index.html'},
     {'title': 'Something More Than This',
      'price': '£16.24',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/something-more-than-this_834/index.html'},
     {'title': 'Soft Apocalypse',
      'price': '£26.12',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/soft-apocalypse_833/index.html'},
     {'title': "So You've Been Publicly Shamed",
      'price': '£12.23',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/so-youve-been-publicly-shamed_832/index.html'},
     {'title': 'Shoe Dog: A Memoir by the Creator of NIKE',
      'price': '£23.99',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/shoe-dog-a-memoir-by-the-creator-of-nike_831/index.html'},
     {'title': 'Shobu Samurai, Project Aryoku (#3)',
      'price': '£29.06',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/shobu-samurai-project-aryoku-3_830/index.html'},
     {'title': 'Secrets and Lace (Fatal Hearts #1)',
      'price': '£20.27',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/secrets-and-lace-fatal-hearts-1_829/index.html'},
     {'title': 'Scarlett Epstein Hates It Here',
      'price': '£43.55',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/scarlett-epstein-hates-it-here_828/index.html'},
     {'title': 'Romero and Juliet: A Tragic Tale of Love and Zombies',
      'price': '£36.94',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/romero-and-juliet-a-tragic-tale-of-love-and-zombies_827/index.html'},
     {'title': 'Redeeming Love',
      'price': '£20.47',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/redeeming-love_826/index.html'},
     {'title': 'Poses for Artists Volume 1 - Dynamic and Sitting Poses: An Essential Reference for Figure Drawing and the Human Form',
      'price': '£41.06',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/poses-for-artists-volume-1-dynamic-and-sitting-poses-an-essential-reference-for-figure-drawing-and-the-human-form_825/index.html'},
     {'title': 'Poems That Make Grown Women Cry',
      'price': '£14.19',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/poems-that-make-grown-women-cry_824/index.html'},
     {'title': 'Nightingale, Sing',
      'price': '£38.28',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/nightingale-sing_823/index.html'},
     {'title': 'Night Sky with Exit Wounds',
      'price': '£41.05',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/night-sky-with-exit-wounds_822/index.html'},
     {'title': 'Mrs. Houdini',
      'price': '£30.25',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/mrs-houdini_821/index.html'},
     {'title': 'Modern Romance',
      'price': '£28.26',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/modern-romance_820/index.html'},
     {'title': 'Miss Peregrine’s Home for Peculiar Children (Miss Peregrine’s Peculiar Children #1)',
      'price': '£10.76',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/miss-peregrines-home-for-peculiar-children-miss-peregrines-peculiar-children-1_819/index.html'},
     {'title': 'Louisa: The Extraordinary Life of Mrs. Adams',
      'price': '£16.85',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/louisa-the-extraordinary-life-of-mrs-adams_818/index.html'},
     {'title': 'Little Red',
      'price': '£13.47',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/little-red_817/index.html'},
     {'title': 'Library of Souls (Miss Peregrine’s Peculiar Children #3)',
      'price': '£48.56',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/library-of-souls-miss-peregrines-peculiar-children-3_816/index.html'},
     {'title': 'Large Print Heart of the Pride',
      'price': '£19.15',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/large-print-heart-of-the-pride_815/index.html'},
     {'title': 'I Had a Nice Time And Other Lies...: How to find love & sh*t like that',
      'price': '£57.36',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/i-had-a-nice-time-and-other-lies-how-to-find-love-sht-like-that_814/index.html'},
     {'title': 'Hollow City (Miss Peregrine’s Peculiar Children #2)',
      'price': '£42.98',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/hollow-city-miss-peregrines-peculiar-children-2_813/index.html'},
     {'title': 'Grumbles',
      'price': '£22.16',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/grumbles_812/index.html'},
     {'title': 'Full Moon over Noah’s Ark: An Odyssey to Mount Ararat and Beyond',
      'price': '£49.43',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html'},
     {'title': 'Frostbite (Vampire Academy #2)',
      'price': '£29.99',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/frostbite-vampire-academy-2_810/index.html'},
     {'title': 'Follow You Home',
      'price': '£21.36',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/follow-you-home_809/index.html'},
     {'title': 'First Steps for New Christians (Print Edition)',
      'price': '£29.00',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/first-steps-for-new-christians-print-edition_808/index.html'},
     {'title': 'Finders Keepers (Bill Hodges Trilogy #2)',
      'price': '£53.53',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/finders-keepers-bill-hodges-trilogy-2_807/index.html'},
     {'title': 'Fables, Vol. 1: Legends in Exile (Fables #1)',
      'price': '£41.62',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/fables-vol-1-legends-in-exile-fables-1_806/index.html'},
     {'title': 'Eureka Trivia 6.0',
      'price': '£54.59',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/eureka-trivia-60_805/index.html'},
     {'title': 'Drive: The Surprising Truth About What Motivates Us',
      'price': '£34.95',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/drive-the-surprising-truth-about-what-motivates-us_804/index.html'},
     {'title': 'Done Rubbed Out (Reightman & Bailey #1)',
      'price': '£37.72',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/done-rubbed-out-reightman-bailey-1_803/index.html'},
     {'title': 'Doing It Over (Most Likely To #1)',
      'price': '£35.61',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/doing-it-over-most-likely-to-1_802/index.html'},
     {'title': 'Deliciously Ella Every Day: Quick and Easy Recipes for Gluten-Free Snacks, Packed Lunches, and Simple Meals',
      'price': '£42.16',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/deliciously-ella-every-day-quick-and-easy-recipes-for-gluten-free-snacks-packed-lunches-and-simple-meals_801/index.html'},
     {'title': 'Dark Notes',
      'price': '£19.19',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/dark-notes_800/index.html'},
     {'title': 'Daring Greatly: How the Courage to Be Vulnerable Transforms the Way We Live, Love, Parent, and Lead',
      'price': '£19.43',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/daring-greatly-how-the-courage-to-be-vulnerable-transforms-the-way-we-live-love-parent-and-lead_799/index.html'},
     {'title': 'Close to You',
      'price': '£49.46',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/close-to-you_798/index.html'},
     {'title': 'Chasing Heaven: What Dying Taught Me About Living',
      'price': '£37.80',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/chasing-heaven-what-dying-taught-me-about-living_797/index.html'},
     {'title': 'Big Magic: Creative Living Beyond Fear',
      'price': '£30.80',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/big-magic-creative-living-beyond-fear_796/index.html'},
     {'title': 'Becoming Wise: An Inquiry into the Mystery and Art of Living',
      'price': '£27.43',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/becoming-wise-an-inquiry-into-the-mystery-and-art-of-living_795/index.html'},
     {'title': 'Beauty Restored (Riley Family Legacy Novellas #3)',
      'price': '£11.11',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/beauty-restored-riley-family-legacy-novellas-3_794/index.html'},
     {'title': 'Batman: The Long Halloween (Batman)',
      'price': '£36.50',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/batman-the-long-halloween-batman_793/index.html'},
     {'title': 'Batman: The Dark Knight Returns (Batman)',
      'price': '£15.38',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/batman-the-dark-knight-returns-batman_792/index.html'},
     {'title': "Ayumi's Violin",
      'price': '£15.48',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/ayumis-violin_791/index.html'},
     {'title': 'Anonymous',
      'price': '£46.82',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/anonymous_790/index.html'},
     {'title': 'Amy Meets the Saints and Sages',
      'price': '£18.46',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/amy-meets-the-saints-and-sages_789/index.html'},
     {'title': 'Amid the Chaos',
      'price': '£36.58',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/amid-the-chaos_788/index.html'},
     {'title': 'Amatus',
      'price': '£50.54',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/amatus_787/index.html'},
     {'title': 'Agnostic: A Spirited Manifesto',
      'price': '£12.51',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/agnostic-a-spirited-manifesto_786/index.html'},
     {'title': 'Zealot: The Life and Times of Jesus of Nazareth',
      'price': '£24.70',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/zealot-the-life-and-times-of-jesus-of-nazareth_785/index.html'},
     {'title': 'You (You #1)',
      'price': '£43.61',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/you-you-1_784/index.html'},
     {'title': 'Wonder Woman: Earth One, Volume One (Wonder Woman: Earth One #1)',
      'price': '£37.34',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/wonder-woman-earth-one-volume-one-wonder-woman-earth-one-1_783/index.html'},
     {'title': 'Wild Swans',
      'price': '£14.36',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/wild-swans_782/index.html'},
     {'title': 'Why the Right Went Wrong: Conservatism--From Goldwater to the Tea Party and Beyond',
      'price': '£52.65',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/why-the-right-went-wrong-conservatism-from-goldwater-to-the-tea-party-and-beyond_781/index.html'},
     {'title': 'Whole Lotta Creativity Going On: 60 Fun and Unusual Exercises to Awaken and Strengthen Your Creativity',
      'price': '£38.20',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/whole-lotta-creativity-going-on-60-fun-and-unusual-exercises-to-awaken-and-strengthen-your-creativity_780/index.html'},
     {'title': "What's It Like in Space?: Stories from Astronauts Who've Been There",
      'price': '£19.60',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/whats-it-like-in-space-stories-from-astronauts-whove-been-there_779/index.html'},
     {'title': 'We Are Robin, Vol. 1: The Vigilante Business (We Are Robin #1)',
      'price': '£53.90',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/we-are-robin-vol-1-the-vigilante-business-we-are-robin-1_778/index.html'},
     {'title': "Walt Disney's Alice in Wonderland",
      'price': '£12.96',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/walt-disneys-alice-in-wonderland_777/index.html'},
     {'title': 'V for Vendetta (V for Vendetta Complete)',
      'price': '£37.10',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/v-for-vendetta-v-for-vendetta-complete_776/index.html'},
     {'title': 'Until Friday Night (The Field Party #1)',
      'price': '£46.31',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/until-friday-night-the-field-party-1_775/index.html'},
     {'title': 'Unbroken: A World War II Story of Survival, Resilience, and Redemption',
      'price': '£45.95',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/unbroken-a-world-war-ii-story-of-survival-resilience-and-redemption_774/index.html'},
     {'title': 'Twenty Yawns',
      'price': '£22.08',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/twenty-yawns_773/index.html'},
     {'title': 'Through the Woods',
      'price': '£25.38',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/through-the-woods_772/index.html'},
     {'title': 'This Is Where It Ends',
      'price': '£27.12',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/this-is-where-it-ends_771/index.html'},
     {'title': 'The Year of Magical Thinking',
      'price': '£43.04',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-year-of-magical-thinking_770/index.html'},
     {'title': 'The Wright Brothers',
      'price': '£56.80',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-wright-brothers_769/index.html'},
     {'title': "The White Queen (The Cousins' War #1)",
      'price': '£25.91',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-white-queen-the-cousins-war-1_768/index.html'},
     {'title': "The Wedding Pact (The O'Malleys #2)",
      'price': '£32.61',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-wedding-pact-the-omalleys-2_767/index.html'},
     {'title': 'The Time Keeper',
      'price': '£27.88',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-time-keeper_766/index.html'},
     {'title': 'The Testament of Mary',
      'price': '£52.67',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-testament-of-mary_765/index.html'},
     {'title': 'The Star-Touched Queen',
      'price': '£46.02',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-star-touched-queen_764/index.html'},
     {'title': 'The Songs of the Gods',
      'price': '£44.48',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-songs-of-the-gods_763/index.html'},
     {'title': 'The Song of Achilles',
      'price': '£37.40',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-song-of-achilles_762/index.html'},
     {'title': 'The Rosie Project (Don Tillman #1)',
      'price': '£54.04',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-rosie-project-don-tillman-1_761/index.html'},
     {'title': 'The Power of Habit: Why We Do What We Do in Life and Business',
      'price': '£16.88',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-power-of-habit-why-we-do-what-we-do-in-life-and-business_760/index.html'},
     {'title': 'The Marriage of Opposites',
      'price': '£28.08',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-marriage-of-opposites_759/index.html'},
     {'title': 'The Lucifer Effect: Understanding How Good People Turn Evil',
      'price': '£10.40',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-lucifer-effect-understanding-how-good-people-turn-evil_758/index.html'},
     {'title': 'The Long Haul (Diary of a Wimpy Kid #9)',
      'price': '£44.07',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-long-haul-diary-of-a-wimpy-kid-9_757/index.html'},
     {'title': 'The Loney',
      'price': '£23.40',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-loney_756/index.html'},
     {'title': 'The Literature Book (Big Ideas Simply Explained)',
      'price': '£17.43',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-literature-book-big-ideas-simply-explained_755/index.html'},
     {'title': 'The Last Mile (Amos Decker #2)',
      'price': '£54.21',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-last-mile-amos-decker-2_754/index.html'},
     {'title': 'The Immortal Life of Henrietta Lacks',
      'price': '£40.67',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-immortal-life-of-henrietta-lacks_753/index.html'},
     {'title': 'The Hidden Oracle (The Trials of Apollo #1)',
      'price': '£52.26',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-hidden-oracle-the-trials-of-apollo-1_752/index.html'},
     {'title': 'The Help Yourself Cookbook for Kids: 60 Easy Plant-Based Recipes Kids Can Make to Stay Healthy and Save the Earth',
      'price': '£28.77',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-help-yourself-cookbook-for-kids-60-easy-plant-based-recipes-kids-can-make-to-stay-healthy-and-save-the-earth_751/index.html'},
     {'title': 'The Guilty (Will Robie #4)',
      'price': '£13.82',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-guilty-will-robie-4_750/index.html'},
     {'title': 'The First Hostage (J.B. Collins #2)',
      'price': '£25.85',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-first-hostage-jb-collins-2_749/index.html'},
     {'title': 'The Dovekeepers',
      'price': '£48.78',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-dovekeepers_748/index.html'},
     {'title': 'The Darkest Lie',
      'price': '£35.35',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-darkest-lie_747/index.html'},
     {'title': 'The Bane Chronicles (The Bane Chronicles #1-11)',
      'price': '£44.73',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-bane-chronicles-the-bane-chronicles-1-11_746/index.html'},
     {'title': 'The Bad-Ass Librarians of Timbuktu: And Their Race to Save the World’s Most Precious Manuscripts',
      'price': '£15.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-bad-ass-librarians-of-timbuktu-and-their-race-to-save-the-worlds-most-precious-manuscripts_745/index.html'},
     {'title': 'The 14th Colony (Cotton Malone #11)',
      'price': '£39.24',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-14th-colony-cotton-malone-11_744/index.html'},
     {'title': 'That Darkness (Gardiner and Renner #1)',
      'price': '£13.92',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/that-darkness-gardiner-and-renner-1_743/index.html'},
     {'title': 'Tastes Like Fear (DI Marnie Rome #3)',
      'price': '£10.69',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/tastes-like-fear-di-marnie-rome-3_742/index.html'},
     {'title': 'Take Me with You',
      'price': '£45.21',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/take-me-with-you_741/index.html'},
     {'title': 'Swell: A Year of Waves',
      'price': '£45.58',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/swell-a-year-of-waves_740/index.html'},
     {'title': 'Superman Vol. 1: Before Truth (Superman by Gene Luen Yang #1)',
      'price': '£11.89',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/superman-vol-1-before-truth-superman-by-gene-luen-yang-1_739/index.html'},
     {'title': 'Still Life with Bread Crumbs',
      'price': '£26.41',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/still-life-with-bread-crumbs_738/index.html'},
     {'title': 'Steve Jobs',
      'price': '£39.50',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/steve-jobs_737/index.html'},
     {'title': 'Sorting the Beef from the Bull: The Science of Food Fraud Forensics',
      'price': '£44.74',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html'},
     {'title': 'Someone Like You (The Harrisons #2)',
      'price': '£52.79',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/someone-like-you-the-harrisons-2_735/index.html'},
     {'title': 'So Cute It Hurts!!, Vol. 6 (So Cute It Hurts!! #6)',
      'price': '£35.43',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/so-cute-it-hurts-vol-6-so-cute-it-hurts-6_734/index.html'},
     {'title': 'Shtum',
      'price': '£55.84',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/shtum_733/index.html'},
     {'title': 'See America: A Celebration of Our National Parks & Treasured Sites',
      'price': '£48.87',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/see-america-a-celebration-of-our-national-parks-treasured-sites_732/index.html'},
     {'title': 'salt.',
      'price': '£46.78',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/salt_731/index.html'},
     {'title': 'Robin War',
      'price': '£47.82',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/robin-war_730/index.html'},
     {'title': 'Red Hood/Arsenal, Vol. 1: Open for Business (Red Hood/Arsenal #1)',
      'price': '£25.48',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/red-hoodarsenal-vol-1-open-for-business-red-hoodarsenal-1_729/index.html'},
     {'title': 'Rain Fish',
      'price': '£23.57',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/rain-fish_728/index.html'},
     {'title': 'Quarter Life Poetry: Poems for the Young, Broke and Hangry',
      'price': '£50.89',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/quarter-life-poetry-poems-for-the-young-broke-and-hangry_727/index.html'},
     {'title': 'Pet Sematary',
      'price': '£10.56',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/pet-sematary_726/index.html'},
     {'title': 'Overload: How to Unplug, Unwind, and Unleash Yourself from the Pressure of Stress',
      'price': '£52.15',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/overload-how-to-unplug-unwind-and-unleash-yourself-from-the-pressure-of-stress_725/index.html'},
     {'title': 'Once Was a Time',
      'price': '£18.28',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/once-was-a-time_724/index.html'},
     {'title': 'Old School (Diary of a Wimpy Kid #10)',
      'price': '£11.83',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/old-school-diary-of-a-wimpy-kid-10_723/index.html'},
     {'title': 'No Dream Is Too High: Life Lessons From a Man Who Walked on the Moon',
      'price': '£21.95',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/no-dream-is-too-high-life-lessons-from-a-man-who-walked-on-the-moon_722/index.html'},
     {'title': 'Naruto (3-in-1 Edition), Vol. 14: Includes Vols. 40, 41 & 42 (Naruto: Omnibus #14)',
      'price': '£38.39',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/naruto-3-in-1-edition-vol-14-includes-vols-40-41-42-naruto-omnibus-14_721/index.html'},
     {'title': 'My Name Is Lucy Barton',
      'price': '£41.56',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/my-name-is-lucy-barton_720/index.html'},
     {'title': 'My Mrs. Brown',
      'price': '£24.48',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/my-mrs-brown_719/index.html'},
     {'title': 'My Kind of Crazy',
      'price': '£40.36',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/my-kind-of-crazy_718/index.html'},
     {'title': 'Mr. Mercedes (Bill Hodges Trilogy #1)',
      'price': '£28.90',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/mr-mercedes-bill-hodges-trilogy-1_717/index.html'},
     {'title': 'More Than Music (Chasing the Dream #1)',
      'price': '£37.61',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/more-than-music-chasing-the-dream-1_716/index.html'},
     {'title': 'Made to Stick: Why Some Ideas Survive and Others Die',
      'price': '£38.85',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/made-to-stick-why-some-ideas-survive-and-others-die_715/index.html'},
     {'title': 'Luis Paints the World',
      'price': '£53.95',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/luis-paints-the-world_714/index.html'},
     {'title': 'Luckiest Girl Alive',
      'price': '£49.83',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/luckiest-girl-alive_713/index.html'},
     {'title': 'Lowriders to the Center of the Earth (Lowriders in Space #2)',
      'price': '£51.51',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/lowriders-to-the-center-of-the-earth-lowriders-in-space-2_712/index.html'},
     {'title': 'Love Is a Mix Tape (Music #1)',
      'price': '£18.03',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/love-is-a-mix-tape-music-1_711/index.html'},
     {'title': 'Looking for Lovely: Collecting the Moments that Matter',
      'price': '£29.14',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/looking-for-lovely-collecting-the-moments-that-matter_710/index.html'},
     {'title': 'Living Leadership by Insight: A Good Leader Achieves, a Great Leader Builds Monuments',
      'price': '£46.91',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/living-leadership-by-insight-a-good-leader-achieves-a-great-leader-builds-monuments_709/index.html'},
     {'title': 'Let It Out: A Journey Through Journaling',
      'price': '£26.79',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/let-it-out-a-journey-through-journaling_708/index.html'},
     {'title': 'Lady Midnight (The Dark Artifices #1)',
      'price': '£16.28',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/lady-midnight-the-dark-artifices-1_707/index.html'},
     {'title': "It's All Easy: Healthy, Delicious Weeknight Meals in under 30 Minutes",
      'price': '£19.55',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/its-all-easy-healthy-delicious-weeknight-meals-in-under-30-minutes_706/index.html'},
     {'title': 'Island of Dragons (Unwanteds #7)',
      'price': '£29.65',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/island-of-dragons-unwanteds-7_705/index.html'},
     {'title': "I Know What I'm Doing -- and Other Lies I Tell Myself: Dispatches from a Life Under Construction",
      'price': '£25.98',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/i-know-what-im-doing-and-other-lies-i-tell-myself-dispatches-from-a-life-under-construction_704/index.html'},
     {'title': 'I Am Pilgrim (Pilgrim #1)',
      'price': '£10.60',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/i-am-pilgrim-pilgrim-1_703/index.html'},
     {'title': 'Hyperbole and a Half: Unfortunate Situations, Flawed Coping Mechanisms, Mayhem, and Other Things That Happened',
      'price': '£14.75',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/hyperbole-and-a-half-unfortunate-situations-flawed-coping-mechanisms-mayhem-and-other-things-that-happened_702/index.html'},
     {'title': 'Hush, Hush (Hush, Hush #1)',
      'price': '£47.02',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/hush-hush-hush-hush-1_701/index.html'},
     {'title': 'Hold Your Breath (Search and Rescue #1)',
      'price': '£28.82',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/hold-your-breath-search-and-rescue-1_700/index.html'},
     {'title': 'Hamilton: The Revolution',
      'price': '£58.79',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/hamilton-the-revolution_699/index.html'},
     {'title': 'Greek Mythic History',
      'price': '£10.23',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/greek-mythic-history_698/index.html'},
     {'title': 'God: The Most Unpleasant Character in All Fiction',
      'price': '£30.03',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/god-the-most-unpleasant-character-in-all-fiction_697/index.html'},
     {'title': 'Glory over Everything: Beyond The Kitchen House',
      'price': '£45.84',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/glory-over-everything-beyond-the-kitchen-house_696/index.html'},
     {'title': 'Feathers: Displays of Brilliant Plumage',
      'price': '£49.05',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/feathers-displays-of-brilliant-plumage_695/index.html'},
     {'title': 'Far & Away: Places on the Brink of Change: Seven Continents, Twenty-Five Years',
      'price': '£15.06',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/far-away-places-on-the-brink-of-change-seven-continents-twenty-five-years_694/index.html'},
     {'title': 'Every Last Word',
      'price': '£46.47',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/every-last-word_693/index.html'},
     {'title': 'Eligible (The Austen Project #4)',
      'price': '£27.09',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/eligible-the-austen-project-4_692/index.html'},
     {'title': 'El Deafo',
      'price': '£57.62',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/el-deafo_691/index.html'},
     {'title': 'Eight Hundred Grapes',
      'price': '£14.39',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/eight-hundred-grapes_690/index.html'},
     {'title': 'Eaternity: More than 150 Deliciously Easy Vegan Recipes for a Long, Healthy, Satisfied, Joyful Life',
      'price': '£51.75',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/eaternity-more-than-150-deliciously-easy-vegan-recipes-for-a-long-healthy-satisfied-joyful-life_689/index.html'},
     {'title': 'Eat Fat, Get Thin',
      'price': '£54.07',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/eat-fat-get-thin_688/index.html'},
     {'title': "Don't Get Caught",
      'price': '£55.35',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/dont-get-caught_687/index.html'},
     {'title': 'Doctor Sleep (The Shining #2)',
      'price': '£40.12',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/doctor-sleep-the-shining-2_686/index.html'},
     {'title': 'Demigods & Magicians: Percy and Annabeth Meet the Kanes (Percy Jackson & Kane Chronicles Crossover #1-3)',
      'price': '£37.51',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/demigods-magicians-percy-and-annabeth-meet-the-kanes-percy-jackson-kane-chronicles-crossover-1-3_685/index.html'},
     {'title': 'Dear Mr. Knightley',
      'price': '£11.21',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/dear-mr-knightley_684/index.html'},
     {'title': 'Daily Fantasy Sports',
      'price': '£36.58',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/daily-fantasy-sports_683/index.html'},
     {'title': 'Crazy Love: Overwhelmed by a Relentless God',
      'price': '£47.72',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/crazy-love-overwhelmed-by-a-relentless-god_682/index.html'},
     {'title': 'Cometh the Hour (The Clifton Chronicles #6)',
      'price': '£25.01',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/cometh-the-hour-the-clifton-chronicles-6_681/index.html'},
     {'title': 'Code Name Verity (Code Name Verity #1)',
      'price': '£22.13',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/code-name-verity-code-name-verity-1_680/index.html'},
     {'title': 'Clockwork Angel (The Infernal Devices #1)',
      'price': '£44.14',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/clockwork-angel-the-infernal-devices-1_679/index.html'},
     {'title': 'City of Glass (The Mortal Instruments #3)',
      'price': '£56.02',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/city-of-glass-the-mortal-instruments-3_678/index.html'},
     {'title': 'City of Fallen Angels (The Mortal Instruments #4)',
      'price': '£11.23',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/city-of-fallen-angels-the-mortal-instruments-4_677/index.html'},
     {'title': 'City of Bones (The Mortal Instruments #1)',
      'price': '£43.28',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/city-of-bones-the-mortal-instruments-1_676/index.html'},
     {'title': 'City of Ashes (The Mortal Instruments #2)',
      'price': '£47.27',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/city-of-ashes-the-mortal-instruments-2_675/index.html'},
     {'title': 'Cell',
      'price': '£20.29',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/cell_674/index.html'},
     {'title': 'Catching Jordan (Hundred Oaks)',
      'price': '£50.83',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/catching-jordan-hundred-oaks_673/index.html'},
     {'title': 'Carry On, Warrior: Thoughts on Life Unarmed',
      'price': '£31.85',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/carry-on-warrior-thoughts-on-life-unarmed_672/index.html'},
     {'title': 'Carrie',
      'price': '£46.23',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/carrie_671/index.html'},
     {'title': 'Buying In: The Secret Dialogue Between What We Buy and Who We Are',
      'price': '£37.80',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/buying-in-the-secret-dialogue-between-what-we-buy-and-who-we-are_670/index.html'},
     {'title': 'Brain on Fire: My Month of Madness',
      'price': '£49.32',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/brain-on-fire-my-month-of-madness_669/index.html'},
     {'title': 'Batman: Europa',
      'price': '£32.01',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/batman-europa_668/index.html'},
     {'title': 'Barefoot Contessa Back to Basics',
      'price': '£28.01',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/barefoot-contessa-back-to-basics_667/index.html'},
     {'title': "Barefoot Contessa at Home: Everyday Recipes You'll Make Over and Over Again",
      'price': '£50.62',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/barefoot-contessa-at-home-everyday-recipes-youll-make-over-and-over-again_666/index.html'},
     {'title': 'Balloon Animals',
      'price': '£17.03',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/balloon-animals_665/index.html'},
     {'title': 'Art Ops Vol. 1',
      'price': '£48.80',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/art-ops-vol-1_664/index.html'},
     {'title': 'Aristotle and Dante Discover the Secrets of the Universe (Aristotle and Dante Discover the Secrets of the Universe #1)',
      'price': '£58.14',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/aristotle-and-dante-discover-the-secrets-of-the-universe-aristotle-and-dante-discover-the-secrets-of-the-universe-1_663/index.html'},
     {'title': 'Angels Walking (Angels Walking #1)',
      'price': '£34.20',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/angels-walking-angels-walking-1_662/index.html'},
     {'title': 'Angels & Demons (Robert Langdon #1)',
      'price': '£51.48',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/angels-demons-robert-langdon-1_661/index.html'},
     {'title': 'All the Light We Cannot See',
      'price': '£29.87',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/all-the-light-we-cannot-see_660/index.html'},
     {'title': 'Adulthood Is a Myth: A "Sarah\'s Scribbles" Collection',
      'price': '£10.90',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/adulthood-is-a-myth-a-sarahs-scribbles-collection_659/index.html'},
     {'title': 'Abstract City',
      'price': '£56.37',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/abstract-city_658/index.html'},
     {'title': 'A Time of Torment (Charlie Parker #14)',
      'price': '£48.35',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/a-time-of-torment-charlie-parker-14_657/index.html'},
     {'title': 'A Study in Scarlet (Sherlock Holmes #1)',
      'price': '£16.73',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/a-study-in-scarlet-sherlock-holmes-1_656/index.html'},
     {'title': 'A Series of Catastrophes and Miracles: A True Story of Love, Science, and Cancer',
      'price': '£56.48',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/a-series-of-catastrophes-and-miracles-a-true-story-of-love-science-and-cancer_655/index.html'},
     {'title': "A People's History of the United States",
      'price': '£40.79',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/a-peoples-history-of-the-united-states_654/index.html'},
     {'title': 'A Man Called Ove',
      'price': '£39.72',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/a-man-called-ove_653/index.html'},
     {'title': 'A Distant Mirror: The Calamitous 14th Century',
      'price': '£14.58',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/a-distant-mirror-the-calamitous-14th-century_652/index.html'},
     {'title': 'A Brush of Wings (Angels Walking #3)',
      'price': '£55.51',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/a-brush-of-wings-angels-walking-3_651/index.html'},
     {'title': '1491: New Revelations of the Americas Before Columbus',
      'price': '£21.80',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/1491-new-revelations-of-the-americas-before-columbus_650/index.html'},
     {'title': 'The Three Searches, Meaning, and the Story',
      'price': '£13.33',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-three-searches-meaning-and-the-story_649/index.html'},
     {'title': 'Searching for Meaning in Gailana',
      'price': '£38.73',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/searching-for-meaning-in-gailana_648/index.html'},
     {'title': 'Rook',
      'price': '£37.86',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/rook_647/index.html'},
     {'title': 'My Kitchen Year: 136 Recipes That Saved My Life',
      'price': '£11.53',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/my-kitchen-year-136-recipes-that-saved-my-life_646/index.html'},
     {'title': '13 Hours: The Inside Account of What Really Happened In Benghazi',
      'price': '£27.06',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/13-hours-the-inside-account-of-what-really-happened-in-benghazi_645/index.html'},
     {'title': "Will You Won't You Want Me?",
      'price': '£13.86',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/will-you-wont-you-want-me_644/index.html'},
     {'title': 'Tipping Point for Planet Earth: How Close Are We to the Edge?',
      'price': '£37.55',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/tipping-point-for-planet-earth-how-close-are-we-to-the-edge_643/index.html'},
     {'title': 'The Star-Touched Queen',
      'price': '£32.30',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-star-touched-queen_642/index.html'},
     {'title': 'The Silent Sister (Riley MacPherson #1)',
      'price': '£46.29',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-silent-sister-riley-macpherson-1_641/index.html'},
     {'title': 'The Midnight Watch: A Novel of the Titanic and the Californian',
      'price': '£26.20',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-midnight-watch-a-novel-of-the-titanic-and-the-californian_640/index.html'},
     {'title': 'The Lonely City: Adventures in the Art of Being Alone',
      'price': '£33.26',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-lonely-city-adventures-in-the-art-of-being-alone_639/index.html'},
     {'title': 'The Gray Rhino: How to Recognize and Act on the Obvious Dangers We Ignore',
      'price': '£59.15',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-gray-rhino-how-to-recognize-and-act-on-the-obvious-dangers-we-ignore_638/index.html'},
     {'title': 'The Golden Condom: And Other Essays on Love Lost and Found',
      'price': '£39.43',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-golden-condom-and-other-essays-on-love-lost-and-found_637/index.html'},
     {'title': 'The Epidemic (The Program 0.6)',
      'price': '£14.44',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-epidemic-the-program-06_636/index.html'},
     {'title': 'The Dinner Party',
      'price': '£56.54',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-dinner-party_635/index.html'},
     {'title': 'The Diary of a Young Girl',
      'price': '£59.90',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-diary-of-a-young-girl_634/index.html'},
     {'title': 'The Children',
      'price': '£11.88',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-children_633/index.html'},
     {'title': 'Stars Above (The Lunar Chronicles #4.5)',
      'price': '£48.05',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/stars-above-the-lunar-chronicles-45_632/index.html'},
     {'title': 'Snatched: How A Drug Queen Went Undercover for the DEA and Was Kidnapped By Colombian Guerillas',
      'price': '£21.21',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/snatched-how-a-drug-queen-went-undercover-for-the-dea-and-was-kidnapped-by-colombian-guerillas_631/index.html'},
     {'title': 'Raspberry Pi Electronics Projects for the Evil Genius',
      'price': '£49.67',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/raspberry-pi-electronics-projects-for-the-evil-genius_630/index.html'},
     {'title': 'Quench Your Own Thirst: Business Lessons Learned Over a Beer or Two',
      'price': '£43.14',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/quench-your-own-thirst-business-lessons-learned-over-a-beer-or-two_629/index.html'},
     {'title': 'Psycho: Sanitarium (Psycho #1.5)',
      'price': '£36.97',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/psycho-sanitarium-psycho-15_628/index.html'},
     {'title': 'Poisonous (Max Revere Novels #3)',
      'price': '£26.80',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/poisonous-max-revere-novels-3_627/index.html'},
     {'title': 'One with You (Crossfire #5)',
      'price': '£15.71',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/one-with-you-crossfire-5_626/index.html'},
     {'title': 'No Love Allowed (Dodge Cove #1)',
      'price': '£54.65',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/no-love-allowed-dodge-cove-1_625/index.html'},
     {'title': 'Murder at the 42nd Street Library (Raymond Ambler #1)',
      'price': '£54.36',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/murder-at-the-42nd-street-library-raymond-ambler-1_624/index.html'},
     {'title': 'Most Wanted',
      'price': '£35.28',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/most-wanted_623/index.html'},
     {'title': 'Love, Lies and Spies',
      'price': '£20.55',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/love-lies-and-spies_622/index.html'},
     {'title': 'How to Speak Golf: An Illustrated Guide to Links Lingo',
      'price': '£58.32',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/how-to-speak-golf-an-illustrated-guide-to-links-lingo_621/index.html'},
     {'title': 'Hide Away (Eve Duncan #20)',
      'price': '£11.84',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/hide-away-eve-duncan-20_620/index.html'},
     {'title': 'Furiously Happy: A Funny Book About Horrible Things',
      'price': '£41.46',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/furiously-happy-a-funny-book-about-horrible-things_619/index.html'},
     {'title': 'Everyday Italian: 125 Simple and Delicious Recipes',
      'price': '£20.10',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/everyday-italian-125-simple-and-delicious-recipes_618/index.html'},
     {'title': "Equal Is Unfair: America's Misguided Fight Against Income Inequality",
      'price': '£56.86',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/equal-is-unfair-americas-misguided-fight-against-income-inequality_617/index.html'},
     {'title': 'Eleanor & Park',
      'price': '£56.51',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/eleanor-park_616/index.html'},
     {'title': 'Dirty (Dive Bar #1)',
      'price': '£40.83',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/dirty-dive-bar-1_615/index.html'},
     {'title': 'Can You Keep a Secret? (Fear Street Relaunch #4)',
      'price': '£48.64',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/can-you-keep-a-secret-fear-street-relaunch-4_614/index.html'},
     {'title': 'Boar Island (Anna Pigeon #19)',
      'price': '£59.48',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/boar-island-anna-pigeon-19_613/index.html'},
     {'title': 'A Paris Apartment',
      'price': '£39.01',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/a-paris-apartment_612/index.html'},
     {'title': 'A la Mode: 120 Recipes in 60 Pairings: Pies, Tarts, Cakes, Crisps, and More Topped with Ice Cream, Gelato, Frozen Custard, and More',
      'price': '£38.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/a-la-mode-120-recipes-in-60-pairings-pies-tarts-cakes-crisps-and-more-topped-with-ice-cream-gelato-frozen-custard-and-more_611/index.html'},
     {'title': 'Troublemaker: Surviving Hollywood and Scientology',
      'price': '£48.39',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/troublemaker-surviving-hollywood-and-scientology_610/index.html'},
     {'title': 'The Widow',
      'price': '£27.26',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-widow_609/index.html'},
     {'title': 'The Sleep Revolution: Transforming Your Life, One Night at a Time',
      'price': '£11.68',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-sleep-revolution-transforming-your-life-one-night-at-a-time_608/index.html'},
     {'title': 'The Improbability of Love',
      'price': '£59.45',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-improbability-of-love_607/index.html'},
     {'title': 'The Art of Startup Fundraising',
      'price': '£21.00',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-art-of-startup-fundraising_606/index.html'},
     {'title': 'Take Me Home Tonight (Rock Star Romance #3)',
      'price': '£53.98',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/take-me-home-tonight-rock-star-romance-3_605/index.html'},
     {'title': 'Sleeping Giants (Themis Files #1)',
      'price': '£48.74',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/sleeping-giants-themis-files-1_604/index.html'},
     {'title': 'Setting the World on Fire: The Brief, Astonishing Life of St. Catherine of Siena',
      'price': '£21.15',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/setting-the-world-on-fire-the-brief-astonishing-life-of-st-catherine-of-siena_603/index.html'},
     {'title': 'Playing with Fire',
      'price': '£13.71',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/playing-with-fire_602/index.html'},
     {'title': 'Off the Hook (Fishing for Trouble #1)',
      'price': '£47.67',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/off-the-hook-fishing-for-trouble-1_601/index.html'},
     {'title': 'Mothering Sunday',
      'price': '£13.34',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/mothering-sunday_600/index.html'},
     {'title': 'Mother, Can You Not?',
      'price': '£16.89',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/mother-can-you-not_599/index.html'},
     {'title': 'M Train',
      'price': '£27.18',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/m-train_598/index.html'},
     {'title': 'Lilac Girls',
      'price': '£17.28',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/lilac-girls_597/index.html'},
     {'title': 'Lies and Other Acts of Love',
      'price': '£45.14',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/lies-and-other-acts-of-love_596/index.html'},
     {'title': 'Lab Girl',
      'price': '£40.85',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/lab-girl_595/index.html'},
     {'title': 'Keep Me Posted',
      'price': '£20.46',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/keep-me-posted_594/index.html'},
     {'title': "It Didn't Start with You: How Inherited Family Trauma Shapes Who We Are and How to End the Cycle",
      'price': '£56.27',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/it-didnt-start-with-you-how-inherited-family-trauma-shapes-who-we-are-and-how-to-end-the-cycle_593/index.html'},
     {'title': 'Grey (Fifty Shades #4)',
      'price': '£48.49',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/grey-fifty-shades-4_592/index.html'},
     {'title': 'Exit, Pursued by a Bear',
      'price': '£51.34',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/exit-pursued-by-a-bear_591/index.html'},
     {'title': 'Daredevils',
      'price': '£16.34',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/daredevils_590/index.html'},
     {'title': 'Cravings: Recipes for What You Want to Eat',
      'price': '£20.50',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/cravings-recipes-for-what-you-want-to-eat_589/index.html'},
     {'title': 'Born for This: How to Find the Work You Were Meant to Do',
      'price': '£21.59',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/born-for-this-how-to-find-the-work-you-were-meant-to-do_588/index.html'},
     {'title': 'Arena',
      'price': '£21.36',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/arena_587/index.html'},
     {'title': 'Adultery',
      'price': '£20.88',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/adultery_586/index.html'},
     {'title': "A Mother's Reckoning: Living in the Aftermath of Tragedy",
      'price': '£19.53',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/a-mothers-reckoning-living-in-the-aftermath-of-tragedy_585/index.html'},
     {'title': "A Gentleman's Position (Society of Gentlemen #3)",
      'price': '£14.75',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/a-gentlemans-position-society-of-gentlemen-3_584/index.html'},
     {'title': '11/22/63',
      'price': '£48.48',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/112263_583/index.html'},
     {'title': '10% Happier: How I Tamed the Voice in My Head, Reduced Stress Without Losing My Edge, and Found Self-Help That Actually Works',
      'price': '£24.57',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/10-happier-how-i-tamed-the-voice-in-my-head-reduced-stress-without-losing-my-edge-and-found-self-help-that-actually-works_582/index.html'},
     {'title': '10-Day Green Smoothie Cleanse: Lose Up to 15 Pounds in 10 Days!',
      'price': '£49.71',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/10-day-green-smoothie-cleanse-lose-up-to-15-pounds-in-10-days_581/index.html'},
     {'title': 'Without Shame',
      'price': '£48.27',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/without-shame_580/index.html'},
     {'title': 'Watchmen',
      'price': '£58.05',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/watchmen_579/index.html'},
     {'title': 'Unlimited Intuition Now',
      'price': '£58.87',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/unlimited-intuition-now_578/index.html'},
     {'title': 'Underlying Notes',
      'price': '£11.82',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/underlying-notes_577/index.html'},
     {'title': 'The Shack',
      'price': '£28.03',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-shack_576/index.html'},
     {'title': 'The New Brand You: Your New Image Makes the Sale for You',
      'price': '£44.05',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-new-brand-you-your-new-image-makes-the-sale-for-you_575/index.html'},
     {'title': 'The Moosewood Cookbook: Recipes from Moosewood Restaurant, Ithaca, New York',
      'price': '£12.34',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-moosewood-cookbook-recipes-from-moosewood-restaurant-ithaca-new-york_574/index.html'},
     {'title': 'The Flowers Lied',
      'price': '£16.68',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-flowers-lied_573/index.html'},
     {'title': 'The Fabric of the Cosmos: Space, Time, and the Texture of Reality',
      'price': '£55.91',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-fabric-of-the-cosmos-space-time-and-the-texture-of-reality_572/index.html'},
     {'title': 'The Book of Mormon',
      'price': '£24.57',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-book-of-mormon_571/index.html'},
     {'title': 'The Art and Science of Low Carbohydrate Living',
      'price': '£52.98',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-art-and-science-of-low-carbohydrate-living_570/index.html'},
     {'title': 'The Alien Club',
      'price': '£54.40',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-alien-club_569/index.html'},
     {'title': 'Suzie Snowflake: One beautiful flake (a self-esteem story)',
      'price': '£54.81',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/suzie-snowflake-one-beautiful-flake-a-self-esteem-story_568/index.html'},
     {'title': 'Nap-a-Roo',
      'price': '£25.08',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/nap-a-roo_567/index.html'},
     {'title': 'NaNo What Now? Finding your editing process, revising your NaNoWriMo book and building a writing career through publishing and beyond',
      'price': '£10.41',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/nano-what-now-finding-your-editing-process-revising-your-nanowrimo-book-and-building-a-writing-career-through-publishing-and-beyond_566/index.html'},
     {'title': 'Modern Day Fables',
      'price': '£47.44',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/modern-day-fables_565/index.html'},
     {'title': "If I Gave You God's Phone Number....: Searching for Spirituality in America",
      'price': '£20.91',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/if-i-gave-you-gods-phone-number-searching-for-spirituality-in-america_564/index.html'},
     {'title': 'Fruits Basket, Vol. 9 (Fruits Basket #9)',
      'price': '£33.95',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/fruits-basket-vol-9-fruits-basket-9_563/index.html'},
     {'title': 'Dress Your Family in Corduroy and Denim',
      'price': '£43.68',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/dress-your-family-in-corduroy-and-denim_562/index.html'},
     {'title': "Don't Forget Steven",
      'price': '£33.23',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/dont-forget-steven_561/index.html'},
     {'title': "Chernobyl 01:23:40: The Incredible True Story of the World's Worst Nuclear Disaster",
      'price': '£35.92',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/chernobyl-012340-the-incredible-true-story-of-the-worlds-worst-nuclear-disaster_560/index.html'},
     {'title': 'Art and Fear: Observations on the Perils (and Rewards) of Artmaking',
      'price': '£48.63',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/art-and-fear-observations-on-the-perils-and-rewards-of-artmaking_559/index.html'},
     {'title': 'A Shard of Ice (The Black Symphony Saga #1)',
      'price': '£56.63',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/a-shard-of-ice-the-black-symphony-saga-1_558/index.html'},
     {'title': "A Hero's Curse (The Unseen Chronicles #1)",
      'price': '£50.49',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/a-heros-curse-the-unseen-chronicles-1_557/index.html'},
     {'title': '23 Degrees South: A Tropical Tale of Changing Whether...',
      'price': '£35.79',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/23-degrees-south-a-tropical-tale-of-changing-whether_556/index.html'},
     {'title': 'Zero to One: Notes on Startups, or How to Build the Future',
      'price': '£34.06',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/zero-to-one-notes-on-startups-or-how-to-build-the-future_555/index.html'},
     {'title': 'Why Not Me?',
      'price': '£17.76',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/why-not-me_554/index.html'},
     {'title': 'When Breath Becomes Air',
      'price': '£39.36',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/when-breath-becomes-air_553/index.html'},
     {'title': 'Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel',
      'price': '£36.94',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/vagabonding-an-uncommon-guide-to-the-art-of-long-term-world-travel_552/index.html'},
     {'title': 'The Unlikely Pilgrimage of Harold Fry (Harold Fry #1)',
      'price': '£43.62',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-unlikely-pilgrimage-of-harold-fry-harold-fry-1_551/index.html'},
     {'title': 'The New Drawing on the Right Side of the Brain',
      'price': '£43.02',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-new-drawing-on-the-right-side-of-the-brain_550/index.html'},
     {'title': "The Midnight Assassin: Panic, Scandal, and the Hunt for America's First Serial Killer",
      'price': '£28.45',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-midnight-assassin-panic-scandal-and-the-hunt-for-americas-first-serial-killer_549/index.html'},
     {'title': 'The Martian (The Martian #1)',
      'price': '£41.39',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-martian-the-martian-1_548/index.html'},
     {'title': 'The High Mountains of Portugal',
      'price': '£51.15',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-high-mountains-of-portugal_547/index.html'},
     {'title': 'The Grownup',
      'price': '£35.88',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-grownup_546/index.html'},
     {'title': "The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It",
      'price': '£36.91',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-e-myth-revisited-why-most-small-businesses-dont-work-and-what-to-do-about-it_545/index.html'},
     {'title': 'South of Sunshine',
      'price': '£28.93',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/south-of-sunshine_544/index.html'},
     {'title': 'Smarter Faster Better: The Secrets of Being Productive in Life and Business',
      'price': '£38.89',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/smarter-faster-better-the-secrets-of-being-productive-in-life-and-business_543/index.html'},
     {'title': 'Silence in the Dark (Logan Point #4)',
      'price': '£58.33',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/silence-in-the-dark-logan-point-4_542/index.html'},
     {'title': 'Shadows of the Past (Logan Point #1)',
      'price': '£39.67',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/shadows-of-the-past-logan-point-1_541/index.html'},
     {'title': 'Roller Girl',
      'price': '£14.10',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/roller-girl_540/index.html'},
     {'title': 'Rising Strong',
      'price': '£21.82',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/rising-strong_539/index.html'},
     {'title': 'Proofs of God: Classical Arguments from Tertullian to Barth',
      'price': '£54.21',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/proofs-of-god-classical-arguments-from-tertullian-to-barth_538/index.html'},
     {'title': 'Please Kill Me: The Uncensored Oral History of Punk',
      'price': '£31.19',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/please-kill-me-the-uncensored-oral-history-of-punk_537/index.html'},
     {'title': 'Out of Print: City Lights Spotlight No. 14',
      'price': '£53.64',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/out-of-print-city-lights-spotlight-no-14_536/index.html'},
     {'title': 'My Life Next Door (My Life Next Door )',
      'price': '£36.39',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/my-life-next-door-my-life-next-door_535/index.html'},
     {'title': "Miller's Valley",
      'price': '£58.54',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/millers-valley_534/index.html'},
     {'title': "Man's Search for Meaning",
      'price': '£29.48',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/mans-search-for-meaning_533/index.html'},
     {'title': "Love That Boy: What Two Presidents, Eight Road Trips, and My Son Taught Me About a Parent's Expectations",
      'price': '£25.06',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/love-that-boy-what-two-presidents-eight-road-trips-and-my-son-taught-me-about-a-parents-expectations_532/index.html'},
     {'title': 'Living Forward: A Proven Plan to Stop Drifting and Get the Life You Want',
      'price': '£12.55',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/living-forward-a-proven-plan-to-stop-drifting-and-get-the-life-you-want_531/index.html'},
     {'title': 'Les Fleurs du Mal',
      'price': '£29.04',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/les-fleurs-du-mal_530/index.html'},
     {'title': 'Left Behind (Left Behind #1)',
      'price': '£40.72',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/left-behind-left-behind-1_529/index.html'},
     {'title': "Kill 'Em and Leave: Searching for James Brown and the American Soul",
      'price': '£45.05',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/kill-em-and-leave-searching-for-james-brown-and-the-american-soul_528/index.html'},
     {'title': 'Kierkegaard: A Christian Missionary to Christians',
      'price': '£47.13',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/kierkegaard-a-christian-missionary-to-christians_527/index.html'},
     {'title': 'John Vassos: Industrial Design for Modern Life',
      'price': '£20.22',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/john-vassos-industrial-design-for-modern-life_526/index.html'},
     {'title': "I'll Give You the Sun",
      'price': '£56.48',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/ill-give-you-the-sun_525/index.html'},
     {'title': 'I Will Find You',
      'price': '£44.21',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/i-will-find-you_524/index.html'},
     {'title': 'Hystopia: A Novel',
      'price': '£21.96',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/hystopia-a-novel_523/index.html'},
     {'title': 'Howl and Other Poems',
      'price': '£40.45',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/howl-and-other-poems_522/index.html'},
     {'title': 'History of Beauty',
      'price': '£10.29',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/history-of-beauty_521/index.html'},
     {'title': "Heaven is for Real: A Little Boy's Astounding Story of His Trip to Heaven and Back",
      'price': '£52.86',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/heaven-is-for-real-a-little-boys-astounding-story-of-his-trip-to-heaven-and-back_520/index.html'},
     {'title': 'Future Shock (Future Shock #1)',
      'price': '£55.65',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/future-shock-future-shock-1_519/index.html'},
     {'title': "Ender's Game (The Ender Quintet #1)",
      'price': '£43.64',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/enders-game-the-ender-quintet-1_518/index.html'},
     {'title': 'Diary of a Citizen Scientist: Chasing Tiger Beetles and Other New Ways of Engaging the World',
      'price': '£28.41',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/diary-of-a-citizen-scientist-chasing-tiger-beetles-and-other-new-ways-of-engaging-the-world_517/index.html'},
     {'title': 'Death by Leisure: A Cautionary Tale',
      'price': '£37.51',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/death-by-leisure-a-cautionary-tale_516/index.html'},
     {'title': 'Brilliant Beacons: A History of the American Lighthouse',
      'price': '£11.45',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/brilliant-beacons-a-history-of-the-american-lighthouse_515/index.html'},
     {'title': "Brazen: The Courage to Find the You That's Been Hiding",
      'price': '£19.22',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/brazen-the-courage-to-find-the-you-thats-been-hiding_514/index.html'},
     {'title': 'Between the World and Me',
      'price': '£56.91',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/between-the-world-and-me_513/index.html'},
     {'title': 'Being Mortal: Medicine and What Matters in the End',
      'price': '£55.06',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/being-mortal-medicine-and-what-matters-in-the-end_512/index.html'},
     {'title': 'A Murder Over a Girl: Justice, Gender, Junior High',
      'price': '£13.20',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/a-murder-over-a-girl-justice-gender-junior-high_511/index.html'},
     {'title': '32 Yolks',
      'price': '£53.63',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/32-yolks_510/index.html'},
     {'title': '"Most Blessed of the Patriarchs": Thomas Jefferson and the Empire of the Imagination',
      'price': '£44.48',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/most-blessed-of-the-patriarchs-thomas-jefferson-and-the-empire-of-the-imagination_509/index.html'},
     {'title': 'You Are a Badass: How to Stop Doubting Your Greatness and Start Living an Awesome Life',
      'price': '£12.08',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/you-are-a-badass-how-to-stop-doubting-your-greatness-and-start-living-an-awesome-life_508/index.html'},
     {'title': 'Wildlife of New York: A Five-Borough Coloring Book',
      'price': '£22.14',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/wildlife-of-new-york-a-five-borough-coloring-book_507/index.html'},
     {'title': 'What Happened on Beale Street (Secrets of the South Mysteries #2)',
      'price': '£25.37',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/what-happened-on-beale-street-secrets-of-the-south-mysteries-2_506/index.html'},
     {'title': 'Unreasonable Hope: Finding Faith in the God Who Brings Purpose to Your Pain',
      'price': '£46.33',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/unreasonable-hope-finding-faith-in-the-god-who-brings-purpose-to-your-pain_505/index.html'},
     {'title': 'Under the Tuscan Sun',
      'price': '£37.33',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/under-the-tuscan-sun_504/index.html'},
     {'title': "Toddlers Are A**holes: It's Not Your Fault",
      'price': '£25.55',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/toddlers-are-aholes-its-not-your-fault_503/index.html'},
     {'title': "The Year of Living Biblically: One Man's Humble Quest to Follow the Bible as Literally as Possible",
      'price': '£34.72',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-year-of-living-biblically-one-mans-humble-quest-to-follow-the-bible-as-literally-as-possible_502/index.html'},
     {'title': 'The Whale',
      'price': '£35.96',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-whale_501/index.html'},
     {'title': 'The Story of Art',
      'price': '£41.14',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-story-of-art_500/index.html'},
     {'title': 'The Origin of Species',
      'price': '£10.01',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-origin-of-species_499/index.html'},
     {'title': 'The Great Gatsby',
      'price': '£36.05',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-great-gatsby_498/index.html'},
     {'title': 'The Good Girl',
      'price': '£49.03',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-good-girl_497/index.html'},
     {'title': 'The Glass Castle',
      'price': '£16.24',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-glass-castle_496/index.html'},
     {'title': "The Faith of Christopher Hitchens: The Restless Soul of the World's Most Notorious Atheist",
      'price': '£39.55',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-faith-of-christopher-hitchens-the-restless-soul-of-the-worlds-most-notorious-atheist_495/index.html'},
     {'title': 'The Drowning Girls',
      'price': '£35.67',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-drowning-girls_494/index.html'},
     {'title': 'The Constant Princess (The Tudor Court #1)',
      'price': '£16.62',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-constant-princess-the-tudor-court-1_493/index.html'},
     {'title': 'The Bourne Identity (Jason Bourne #1)',
      'price': '£42.78',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-bourne-identity-jason-bourne-1_492/index.html'},
     {'title': "The Bachelor Girl's Guide to Murder (Herringford and Watts Mysteries #1)",
      'price': '£52.30',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-bachelor-girls-guide-to-murder-herringford-and-watts-mysteries-1_491/index.html'},
     {'title': 'The Art Book',
      'price': '£32.34',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-art-book_490/index.html'},
     {'title': 'The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change',
      'price': '£33.17',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-7-habits-of-highly-effective-people-powerful-lessons-in-personal-change_489/index.html'},
     {'title': 'Team of Rivals: The Political Genius of Abraham Lincoln',
      'price': '£20.12',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/team-of-rivals-the-political-genius-of-abraham-lincoln_488/index.html'},
     {'title': 'Steal Like an Artist: 10 Things Nobody Told You About Being Creative',
      'price': '£20.90',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/steal-like-an-artist-10-things-nobody-told-you-about-being-creative_487/index.html'},
     {'title': 'Sit, Stay, Love',
      'price': '£20.90',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/sit-stay-love_486/index.html'},
     {'title': 'Sister Dear',
      'price': '£40.20',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/sister-dear_485/index.html'},
     {'title': 'Shrunken Treasures: Literary Classics, Short, Sweet, and Silly',
      'price': '£52.87',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/shrunken-treasures-literary-classics-short-sweet-and-silly_484/index.html'},
     {'title': 'Rich Dad, Poor Dad',
      'price': '£51.74',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/rich-dad-poor-dad_483/index.html'},
     {'title': 'Raymie Nightingale',
      'price': '£34.41',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/raymie-nightingale_482/index.html'},
     {'title': 'Playing from the Heart',
      'price': '£32.38',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/playing-from-the-heart_481/index.html'},
     {'title': 'Nightstruck: A Novel',
      'price': '£50.35',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/nightstruck-a-novel_480/index.html'},
     {'title': 'Naturally Lean: 125 Nourishing Gluten-Free, Plant-Based Recipes--All Under 300 Calories',
      'price': '£11.38',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/naturally-lean-125-nourishing-gluten-free-plant-based-recipes-all-under-300-calories_479/index.html'},
     {'title': 'Meternity',
      'price': '£43.58',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/meternity_478/index.html'},
     {'title': 'Memoirs of a Geisha',
      'price': '£49.67',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/memoirs-of-a-geisha_477/index.html'},
     {'title': 'Like Never Before (Walker Family #2)',
      'price': '£28.77',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/like-never-before-walker-family-2_476/index.html'},
     {'title': 'Life of Pi',
      'price': '£13.22',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/life-of-pi_475/index.html'},
     {'title': 'Leave This Song Behind: Teen Poetry at Its Best',
      'price': '£51.17',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/leave-this-song-behind-teen-poetry-at-its-best_474/index.html'},
     {'title': "King's Folly (The Kinsman Chronicles #1)",
      'price': '£39.61',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/kings-folly-the-kinsman-chronicles-1_473/index.html'},
     {'title': 'John Adams',
      'price': '£57.43',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/john-adams_472/index.html'},
     {'title': 'How to Cook Everything Vegetarian: Simple Meatless Recipes for Great Food (How to Cook Everything)',
      'price': '£46.01',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/how-to-cook-everything-vegetarian-simple-meatless-recipes-for-great-food-how-to-cook-everything_471/index.html'},
     {'title': 'How to Be a Domestic Goddess: Baking and the Art of Comfort Cooking',
      'price': '£28.25',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/how-to-be-a-domestic-goddess-baking-and-the-art-of-comfort-cooking_470/index.html'},
     {'title': 'Good in Bed (Cannie Shapiro #1)',
      'price': '£37.05',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/good-in-bed-cannie-shapiro-1_469/index.html'},
     {'title': 'Fruits Basket, Vol. 7 (Fruits Basket #7)',
      'price': '£19.57',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/fruits-basket-vol-7-fruits-basket-7_468/index.html'},
     {'title': 'For the Love: Fighting for Grace in a World of Impossible Standards',
      'price': '£45.13',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/for-the-love-fighting-for-grace-in-a-world-of-impossible-standards_467/index.html'},
     {'title': 'Finding God in the Ruins: How God Redeems Pain',
      'price': '£46.64',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/finding-god-in-the-ruins-how-god-redeems-pain_466/index.html'},
     {'title': 'Every Heart a Doorway (Every Heart A Doorway #1)',
      'price': '£12.16',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/every-heart-a-doorway-every-heart-a-doorway-1_465/index.html'},
     {'title': 'Delivering the Truth (Quaker Midwife Mystery #1)',
      'price': '£20.89',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/delivering-the-truth-quaker-midwife-mystery-1_464/index.html'},
     {'title': 'Counted With the Stars (Out from Egypt #1)',
      'price': '£17.97',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/counted-with-the-stars-out-from-egypt-1_463/index.html'},
     {'title': 'Chronicles, Vol. 1',
      'price': '£52.60',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/chronicles-vol-1_462/index.html'},
     {'title': 'Blue Like Jazz: Nonreligious Thoughts on Christian Spirituality',
      'price': '£25.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/blue-like-jazz-nonreligious-thoughts-on-christian-spirituality_461/index.html'},
     {'title': 'Benjamin Franklin: An American Life',
      'price': '£48.19',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/benjamin-franklin-an-american-life_460/index.html'},
     {'title': 'At The Existentialist Café: Freedom, Being, and apricot cocktails with: Jean-Paul Sartre, Simone de Beauvoir, Albert Camus, Martin Heidegger, Edmund Husserl, Karl Jaspers, Maurice Merleau-Ponty and others',
      'price': '£29.93',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/at-the-existentialist-cafe-freedom-being-and-apricot-cocktails-with-jean-paul-sartre-simone-de-beauvoir-albert-camus-martin-heidegger-edmund-husserl-karl-jaspers-maurice-merleau-ponty-and-others_459/index.html'},
     {'title': 'A Summer In Europe',
      'price': '£44.34',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/a-summer-in-europe_458/index.html'},
     {'title': 'A Short History of Nearly Everything',
      'price': '£52.40',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/a-short-history-of-nearly-everything_457/index.html'},
     {'title': 'A Gathering of Shadows (Shades of Magic #2)',
      'price': '£44.81',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/a-gathering-of-shadows-shades-of-magic-2_456/index.html'},
     {'title': 'The Sound Of Love',
      'price': '£57.84',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-sound-of-love_455/index.html'},
     {'title': 'The Rise and Fall of the Third Reich: A History of Nazi Germany',
      'price': '£39.67',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-rise-and-fall-of-the-third-reich-a-history-of-nazi-germany_454/index.html'},
     {'title': 'The Perks of Being a Wallflower',
      'price': '£55.02',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-perks-of-being-a-wallflower_453/index.html'},
     {'title': 'The Mysterious Affair at Styles (Hercule Poirot #1)',
      'price': '£24.80',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html'},
     {'title': 'The Man Who Mistook His Wife for a Hat and Other Clinical Tales',
      'price': '£59.45',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-man-who-mistook-his-wife-for-a-hat-and-other-clinical-tales_451/index.html'},
     {'title': 'The Makings of a Fatherless Child',
      'price': '£31.58',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-makings-of-a-fatherless-child_450/index.html'},
     {'title': 'The Joy of Cooking',
      'price': '£43.27',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-joy-of-cooking_449/index.html'},
     {'title': 'The Invention of Wings',
      'price': '£37.34',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-invention-of-wings_448/index.html'},
     {'title': 'The Hobbit (Middle-Earth Universe)',
      'price': '£17.80',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-hobbit-middle-earth-universe_447/index.html'},
     {'title': 'The Great Railway Bazaar',
      'price': '£30.54',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-great-railway-bazaar_446/index.html'},
     {'title': 'The Golden Compass (His Dark Materials #1)',
      'price': '£18.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-golden-compass-his-dark-materials-1_445/index.html'},
     {'title': 'The God Delusion',
      'price': '£46.85',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-god-delusion_444/index.html'},
     {'title': 'The Girl You Left Behind (The Girl You Left Behind #1)',
      'price': '£15.79',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-girl-you-left-behind-the-girl-you-left-behind-1_443/index.html'},
     {'title': 'The Fellowship of the Ring (The Lord of the Rings #1)',
      'price': '£10.27',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-fellowship-of-the-ring-the-lord-of-the-rings-1_442/index.html'},
     {'title': 'The Collected Poems of W.B. Yeats (The Collected Works of W.B. Yeats #1)',
      'price': '£15.42',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-collected-poems-of-wb-yeats-the-collected-works-of-wb-yeats-1_441/index.html'},
     {'title': 'The Barefoot Contessa Cookbook',
      'price': '£59.92',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-barefoot-contessa-cookbook_440/index.html'},
     {'title': "Tell the Wolves I'm Home",
      'price': '£50.96',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/tell-the-wolves-im-home_439/index.html'},
     {'title': 'Ship Leaves Harbor: Essays on Travel by a Recovering Journeyman',
      'price': '£30.60',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/ship-leaves-harbor-essays-on-travel-by-a-recovering-journeyman_438/index.html'},
     {'title': 'Pride and Prejudice',
      'price': '£19.27',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/pride-and-prejudice_437/index.html'},
     {'title': 'Musicophilia: Tales of Music and the Brain',
      'price': '£46.58',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/musicophilia-tales-of-music-and-the-brain_436/index.html'},
     {'title': 'Mere Christianity',
      'price': '£48.51',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/mere-christianity_435/index.html'},
     {'title': 'Me Before You (Me Before You #1)',
      'price': '£19.02',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/me-before-you-me-before-you-1_434/index.html'},
     {'title': 'In the Woods (Dublin Murder Squad #1)',
      'price': '£38.38',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/in-the-woods-dublin-murder-squad-1_433/index.html'},
     {'title': 'In Cold Blood',
      'price': '£49.98',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/in-cold-blood_432/index.html'},
     {'title': 'How to Stop Worrying and Start Living',
      'price': '£46.49',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/how-to-stop-worrying-and-start-living_431/index.html'},
     {'title': 'Give It Back',
      'price': '£18.32',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/give-it-back_430/index.html'},
     {'title': 'Girl, Interrupted',
      'price': '£42.14',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/girl-interrupted_429/index.html'},
     {'title': 'Fun Home: A Family Tragicomic',
      'price': '£56.59',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/fun-home-a-family-tragicomic_428/index.html'},
     {'title': 'Fruits Basket, Vol. 6 (Fruits Basket #6)',
      'price': '£20.96',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/fruits-basket-vol-6-fruits-basket-6_427/index.html'},
     {'title': 'Deception Point',
      'price': '£40.32',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/deception-point_426/index.html'},
     {'title': 'Death Note, Vol. 6: Give-and-Take (Death Note #6)',
      'price': '£36.39',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/death-note-vol-6-give-and-take-death-note-6_425/index.html'},
     {'title': 'Catherine the Great: Portrait of a Woman',
      'price': '£58.55',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/catherine-the-great-portrait-of-a-woman_424/index.html'},
     {'title': 'Better Homes and Gardens New Cook Book',
      'price': '£39.61',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/better-homes-and-gardens-new-cook-book_423/index.html'},
     {'title': 'An Unquiet Mind: A Memoir of Moods and Madness',
      'price': '£21.30',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/an-unquiet-mind-a-memoir-of-moods-and-madness_422/index.html'},
     {'title': 'A Year in Provence (Provence #1)',
      'price': '£56.88',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/a-year-in-provence-provence-1_421/index.html'},
     {'title': 'World Without End (The Pillars of the Earth #2)',
      'price': '£32.97',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/world-without-end-the-pillars-of-the-earth-2_420/index.html'},
     {'title': 'Will Grayson, Will Grayson (Will Grayson, Will Grayson)',
      'price': '£47.31',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/will-grayson-will-grayson-will-grayson-will-grayson_419/index.html'},
     {'title': 'Why Save the Bankers?: And Other Essays on Our Economic and Political Crisis',
      'price': '£48.67',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/why-save-the-bankers-and-other-essays-on-our-economic-and-political-crisis_418/index.html'},
     {'title': 'Where She Went (If I Stay #2)',
      'price': '£41.73',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/where-she-went-if-i-stay-2_417/index.html'},
     {'title': 'What If?: Serious Scientific Answers to Absurd Hypothetical Questions',
      'price': '£53.68',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/what-if-serious-scientific-answers-to-absurd-hypothetical-questions_416/index.html'},
     {'title': 'Two Summers',
      'price': '£14.64',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/two-summers_415/index.html'},
     {'title': 'This Is Your Brain on Music: The Science of a Human Obsession',
      'price': '£38.40',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/this-is-your-brain-on-music-the-science-of-a-human-obsession_414/index.html'},
     {'title': 'The Secret Garden',
      'price': '£15.08',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-secret-garden_413/index.html'},
     {'title': 'The Raven King (The Raven Cycle #4)',
      'price': '£30.57',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-raven-king-the-raven-cycle-4_412/index.html'},
     {'title': 'The Raven Boys (The Raven Cycle #1)',
      'price': '£57.74',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-raven-boys-the-raven-cycle-1_411/index.html'},
     {'title': 'The Power Greens Cookbook: 140 Delicious Superfood Recipes',
      'price': '£11.05',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-power-greens-cookbook-140-delicious-superfood-recipes_410/index.html'},
     {'title': 'The Metamorphosis',
      'price': '£28.58',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-metamorphosis_409/index.html'},
     {'title': "The Mathews Men: Seven Brothers and the War Against Hitler's U-boats",
      'price': '£42.91',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-mathews-men-seven-brothers-and-the-war-against-hitlers-u-boats_408/index.html'},
     {'title': 'The Little Paris Bookshop',
      'price': '£24.73',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-little-paris-bookshop_407/index.html'},
     {'title': 'The Hiding Place',
      'price': '£55.91',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-hiding-place_406/index.html'},
     {'title': 'The Grand Design',
      'price': '£13.76',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-grand-design_405/index.html'},
     {'title': 'The Firm',
      'price': '£45.56',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-firm_404/index.html'},
     {'title': 'The Fault in Our Stars',
      'price': '£47.22',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-fault-in-our-stars_403/index.html'},
     {'title': 'The False Prince (The Ascendance Trilogy #1)',
      'price': '£56.00',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-false-prince-the-ascendance-trilogy-1_402/index.html'},
     {'title': 'The Expatriates',
      'price': '£44.58',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-expatriates_401/index.html'},
     {'title': 'The Dream Thieves (The Raven Cycle #2)',
      'price': '£34.50',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-dream-thieves-the-raven-cycle-2_400/index.html'},
     {'title': 'The Darkest Corners',
      'price': '£11.33',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-darkest-corners_399/index.html'},
     {'title': 'The Crossover',
      'price': '£38.77',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-crossover_398/index.html'},
     {'title': 'The 5th Wave (The 5th Wave #1)',
      'price': '£11.83',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-5th-wave-the-5th-wave-1_397/index.html'},
     {'title': 'Tell the Wind and Fire',
      'price': '£45.51',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/tell-the-wind-and-fire_396/index.html'},
     {'title': 'Tell Me Three Things',
      'price': '£41.81',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/tell-me-three-things_395/index.html'},
     {'title': "Talking to Girls About Duran Duran: One Young Man's Quest for True Love and a Cooler Haircut",
      'price': '£25.15',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/talking-to-girls-about-duran-duran-one-young-mans-quest-for-true-love-and-a-cooler-haircut_394/index.html'},
     {'title': 'Siddhartha',
      'price': '£34.22',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/siddhartha_393/index.html'},
     {'title': 'Shiver (The Wolves of Mercy Falls #1)',
      'price': '£16.23',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/shiver-the-wolves-of-mercy-falls-1_392/index.html'},
     {'title': 'Remember Me?',
      'price': '£11.48',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/remember-me_391/index.html'},
     {'title': 'Red Dragon (Hannibal Lecter #1)',
      'price': '£23.37',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/red-dragon-hannibal-lecter-1_390/index.html'},
     {'title': 'Peak: Secrets from the New Science of Expertise',
      'price': '£16.28',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/peak-secrets-from-the-new-science-of-expertise_389/index.html'},
     {'title': 'My Mother Was Nuts',
      'price': '£31.63',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/my-mother-was-nuts_388/index.html'},
     {'title': 'Mexican Today: New and Rediscovered Recipes for Contemporary Kitchens',
      'price': '£24.91',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/mexican-today-new-and-rediscovered-recipes-for-contemporary-kitchens_387/index.html'},
     {'title': 'Maybe Something Beautiful: How Art Transformed a Neighborhood',
      'price': '£22.54',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/maybe-something-beautiful-how-art-transformed-a-neighborhood_386/index.html'},
     {'title': 'Lola and the Boy Next Door (Anna and the French Kiss #2)',
      'price': '£23.63',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/lola-and-the-boy-next-door-anna-and-the-french-kiss-2_385/index.html'},
     {'title': 'Logan Kade (Fallen Crest High #5.5)',
      'price': '£13.12',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/logan-kade-fallen-crest-high-55_384/index.html'},
     {'title': 'Last One Home (New Beginnings #1)',
      'price': '£59.98',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/last-one-home-new-beginnings-1_383/index.html'},
     {'title': 'Killing Floor (Jack Reacher #1)',
      'price': '£31.49',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/killing-floor-jack-reacher-1_382/index.html'},
     {'title': 'Kill the Boy Band',
      'price': '£15.52',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/kill-the-boy-band_381/index.html'},
     {'title': 'Isla and the Happily Ever After (Anna and the French Kiss #3)',
      'price': '£48.13',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/isla-and-the-happily-ever-after-anna-and-the-french-kiss-3_380/index.html'},
     {'title': 'If I Stay (If I Stay #1)',
      'price': '£38.13',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/if-i-stay-if-i-stay-1_379/index.html'},
     {'title': "I Know Why the Caged Bird Sings (Maya Angelou's Autobiography #1)",
      'price': '£36.55',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/i-know-why-the-caged-bird-sings-maya-angelous-autobiography-1_378/index.html'},
     {'title': 'Harry Potter and the Deathly Hallows (Harry Potter #7)',
      'price': '£23.32',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/harry-potter-and-the-deathly-hallows-harry-potter-7_377/index.html'},
     {'title': 'Fruits Basket, Vol. 5 (Fruits Basket #5)',
      'price': '£16.33',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/fruits-basket-vol-5-fruits-basket-5_376/index.html'},
     {'title': 'Foundation (Foundation (Publication Order) #1)',
      'price': '£32.42',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/foundation-foundation-publication-order-1_375/index.html'},
     {'title': 'Fool Me Once',
      'price': '£16.96',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/fool-me-once_374/index.html'},
     {'title': 'Find Her (Detective D.D. Warren #8)',
      'price': '£22.37',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/find-her-detective-dd-warren-8_373/index.html'},
     {'title': 'Evicted: Poverty and Profit in the American City',
      'price': '£42.27',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/evicted-poverty-and-profit-in-the-american-city_372/index.html'},
     {'title': 'Drama',
      'price': '£38.70',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/drama_371/index.html'},
     {'title': 'Dracula the Un-Dead',
      'price': '£35.63',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/dracula-the-un-dead_370/index.html'},
     {'title': 'Digital Fortress',
      'price': '£58.00',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/digital-fortress_369/index.html'},
     {'title': 'Death Note, Vol. 5: Whiteout (Death Note #5)',
      'price': '£52.41',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/death-note-vol-5-whiteout-death-note-5_368/index.html'},
     {'title': 'Data, A Love Story: How I Gamed Online Dating to Meet My Match',
      'price': '£32.35',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/data-a-love-story-how-i-gamed-online-dating-to-meet-my-match_367/index.html'},
     {'title': 'Critique of Pure Reason',
      'price': '£20.75',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/critique-of-pure-reason_366/index.html'},
     {'title': 'Booked',
      'price': '£17.49',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/booked_365/index.html'},
     {'title': 'Blue Lily, Lily Blue (The Raven Cycle #3)',
      'price': '£34.13',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/blue-lily-lily-blue-the-raven-cycle-3_364/index.html'},
     {'title': 'Approval Junkie: Adventures in Caring Too Much',
      'price': '£58.81',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/approval-junkie-adventures-in-caring-too-much_363/index.html'},
     {'title': 'An Abundance of Katherines',
      'price': '£10.00',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/an-abundance-of-katherines_362/index.html'},
     {'title': "America's War for the Greater Middle East: A Military History",
      'price': '£51.22',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/americas-war-for-the-greater-middle-east-a-military-history_361/index.html'},
     {'title': 'Alight (The Generations Trilogy #2)',
      'price': '£58.59',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/alight-the-generations-trilogy-2_360/index.html'},
     {'title': "A Girl's Guide to Moving On (New Beginnings #2)",
      'price': '£31.30',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/a-girls-guide-to-moving-on-new-beginnings-2_359/index.html'},
     {'title': 'A Game of Thrones (A Song of Ice and Fire #1)',
      'price': '£46.42',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/a-game-of-thrones-a-song-of-ice-and-fire-1_358/index.html'},
     {'title': 'A Feast for Crows (A Song of Ice and Fire #4)',
      'price': '£17.21',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/a-feast-for-crows-a-song-of-ice-and-fire-4_357/index.html'},
     {'title': 'A Clash of Kings (A Song of Ice and Fire #2)',
      'price': '£10.79',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/a-clash-of-kings-a-song-of-ice-and-fire-2_356/index.html'},
     {'title': 'Vogue Colors A to Z: A Fashion Coloring Book',
      'price': '£52.35',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/vogue-colors-a-to-z-a-fashion-coloring-book_355/index.html'},
     {'title': 'The Shining (The Shining #1)',
      'price': '£27.88',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-shining-the-shining-1_354/index.html'},
     {'title': "The Pilgrim's Progress",
      'price': '£50.26',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-pilgrims-progress_353/index.html'},
     {'title': 'The Perfect Play (Play by Play #1)',
      'price': '£59.99',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-perfect-play-play-by-play-1_352/index.html'},
     {'title': 'The Passion of Dolssa',
      'price': '£28.32',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-passion-of-dolssa_351/index.html'},
     {'title': 'The Jazz of Physics: The Secret Link Between Music and the Structure of the Universe',
      'price': '£38.71',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-jazz-of-physics-the-secret-link-between-music-and-the-structure-of-the-universe_350/index.html'},
     {'title': 'The Hunger Games (The Hunger Games #1)',
      'price': '£29.85',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-hunger-games-the-hunger-games-1_349/index.html'},
     {'title': 'The Hound of the Baskervilles (Sherlock Holmes #5)',
      'price': '£14.82',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-hound-of-the-baskervilles-sherlock-holmes-5_348/index.html'},
     {'title': 'The Gunning of America: Business and the Making of American Gun Culture',
      'price': '£16.81',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-gunning-of-america-business-and-the-making-of-american-gun-culture_347/index.html'},
     {'title': "The Geography of Bliss: One Grump's Search for the Happiest Places in the World",
      'price': '£28.23',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-geography-of-bliss-one-grumps-search-for-the-happiest-places-in-the-world_346/index.html'},
     {'title': 'The Demonists (Demonist #1)',
      'price': '£52.11',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-demonists-demonist-1_345/index.html'},
     {'title': 'The Demon Prince of Momochi House, Vol. 4 (The Demon Prince of Momochi House #4)',
      'price': '£27.88',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-demon-prince-of-momochi-house-vol-4-the-demon-prince-of-momochi-house-4_344/index.html'},
     {'title': 'The Bone Hunters (Lexy Vaughan & Steven Macaulay #2)',
      'price': '£59.71',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-bone-hunters-lexy-vaughan-steven-macaulay-2_343/index.html'},
     {'title': 'The Beast (Black Dagger Brotherhood #14)',
      'price': '£46.08',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-beast-black-dagger-brotherhood-14_342/index.html'},
     {'title': 'Some Women',
      'price': '£13.73',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/some-women_341/index.html'},
     {'title': 'Shopaholic Ties the Knot (Shopaholic #3)',
      'price': '£48.39',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/shopaholic-ties-the-knot-shopaholic-3_340/index.html'},
     {'title': 'Paper and Fire (The Great Library #2)',
      'price': '£49.45',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/paper-and-fire-the-great-library-2_339/index.html'},
     {'title': 'Outlander (Outlander #1)',
      'price': '£19.67',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/outlander-outlander-1_338/index.html'},
     {'title': 'Orchestra of Exiles: The Story of Bronislaw Huberman, the Israel Philharmonic, and the One Thousand Jews He Saved from Nazi Horrors',
      'price': '£12.36',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/orchestra-of-exiles-the-story-of-bronislaw-huberman-the-israel-philharmonic-and-the-one-thousand-jews-he-saved-from-nazi-horrors_337/index.html'},
     {'title': 'No One Here Gets Out Alive',
      'price': '£20.02',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/no-one-here-gets-out-alive_336/index.html'},
     {'title': 'Night Shift (Night Shift #1-20)',
      'price': '£12.75',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/night-shift-night-shift-1-20_335/index.html'},
     {'title': 'Needful Things',
      'price': '£47.51',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/needful-things_334/index.html'},
     {'title': 'Mockingjay (The Hunger Games #3)',
      'price': '£20.44',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/mockingjay-the-hunger-games-3_333/index.html'},
     {'title': 'Misery',
      'price': '£34.79',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/misery_332/index.html'},
     {'title': 'Little Women (Little Women #1)',
      'price': '£28.07',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/little-women-little-women-1_331/index.html'},
     {'title': 'It',
      'price': '£25.01',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/it_330/index.html'},
     {'title': "Harry Potter and the Sorcerer's Stone (Harry Potter #1)",
      'price': '£13.90',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/harry-potter-and-the-sorcerers-stone-harry-potter-1_329/index.html'},
     {'title': 'Harry Potter and the Prisoner of Azkaban (Harry Potter #3)',
      'price': '£24.17',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/harry-potter-and-the-prisoner-of-azkaban-harry-potter-3_328/index.html'},
     {'title': 'Harry Potter and the Order of the Phoenix (Harry Potter #5)',
      'price': '£31.63',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/harry-potter-and-the-order-of-the-phoenix-harry-potter-5_327/index.html'},
     {'title': 'Harry Potter and the Half-Blood Prince (Harry Potter #6)',
      'price': '£48.75',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/harry-potter-and-the-half-blood-prince-harry-potter-6_326/index.html'},
     {'title': 'Harry Potter and the Chamber of Secrets (Harry Potter #2)',
      'price': '£14.74',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/harry-potter-and-the-chamber-of-secrets-harry-potter-2_325/index.html'},
     {'title': 'Gone with the Wind',
      'price': '£32.49',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/gone-with-the-wind_324/index.html'},
     {'title': 'God Is Not Great: How Religion Poisons Everything',
      'price': '£27.80',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/god-is-not-great-how-religion-poisons-everything_323/index.html'},
     {'title': 'Girl With a Pearl Earring',
      'price': '£26.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/girl-with-a-pearl-earring_322/index.html'},
     {'title': 'Fruits Basket, Vol. 4 (Fruits Basket #4)',
      'price': '£50.44',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/fruits-basket-vol-4-fruits-basket-4_321/index.html'},
     {'title': 'Far From True (Promise Falls Trilogy #2)',
      'price': '£34.93',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/far-from-true-promise-falls-trilogy-2_320/index.html'},
     {'title': 'Dark Lover (Black Dagger Brotherhood #1)',
      'price': '£12.87',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/dark-lover-black-dagger-brotherhood-1_319/index.html'},
     {'title': 'Confessions of a Shopaholic (Shopaholic #1)',
      'price': '£48.94',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/confessions-of-a-shopaholic-shopaholic-1_318/index.html'},
     {'title': 'Changing the Game (Play by Play #2)',
      'price': '£13.38',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/changing-the-game-play-by-play-2_317/index.html'},
     {'title': 'Candide',
      'price': '£58.63',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/candide_316/index.html'},
     {'title': 'Can You Keep a Secret?',
      'price': '£21.94',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/can-you-keep-a-secret_315/index.html'},
     {'title': 'Atlas Shrugged',
      'price': '£26.58',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/atlas-shrugged_314/index.html'},
     {'title': 'Animal Farm',
      'price': '£57.22',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/animal-farm_313/index.html'},
     {'title': 'A Walk to Remember',
      'price': '£56.43',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/a-walk-to-remember_312/index.html'},
     {'title': "A New Earth: Awakening to Your Life's Purpose",
      'price': '£55.65',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/a-new-earth-awakening-to-your-lifes-purpose_311/index.html'},
     {'title': 'A History of God: The 4,000-Year Quest of Judaism, Christianity, and Islam',
      'price': '£27.62',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/a-history-of-god-the-4000-year-quest-of-judaism-christianity-and-islam_310/index.html'},
     {'title': "'Salem's Lot",
      'price': '£49.56',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/salems-lot_309/index.html'},
     {'title': 'Zero History (Blue Ant #3)',
      'price': '£34.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/zero-history-blue-ant-3_308/index.html'},
     {'title': 'Wuthering Heights',
      'price': '£17.73',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/wuthering-heights_307/index.html'},
     {'title': 'World War Z: An Oral History of the Zombie War',
      'price': '£21.80',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/world-war-z-an-oral-history-of-the-zombie-war_306/index.html'},
     {'title': 'Wild: From Lost to Found on the Pacific Crest Trail',
      'price': '£46.02',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/wild-from-lost-to-found-on-the-pacific-crest-trail_305/index.html'},
     {'title': "Where'd You Go, Bernadette",
      'price': '£18.13',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/whered-you-go-bernadette_304/index.html'},
     {'title': 'When You Are Engulfed in Flames',
      'price': '£30.89',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/when-you-are-engulfed-in-flames_303/index.html'},
     {'title': "We the People: The Modern-Day Figures Who Have Reshaped and Affirmed the Founding Fathers' Vision of America",
      'price': '£31.95',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/we-the-people-the-modern-day-figures-who-have-reshaped-and-affirmed-the-founding-fathers-vision-of-america_302/index.html'},
     {'title': 'We Are All Completely Beside Ourselves',
      'price': '£24.04',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/we-are-all-completely-beside-ourselves_301/index.html'},
     {'title': 'Walk the Edge (Thunder Road #2)',
      'price': '£32.36',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/walk-the-edge-thunder-road-2_300/index.html'},
     {'title': 'Voyager (Outlander #3)',
      'price': '£21.07',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/voyager-outlander-3_299/index.html'},
     {'title': 'Very Good Lives: The Fringe Benefits of Failure and the Importance of Imagination',
      'price': '£50.66',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/very-good-lives-the-fringe-benefits-of-failure-and-the-importance-of-imagination_298/index.html'},
     {'title': 'Vegan Vegetarian Omnivore: Dinner for Everyone at the Table',
      'price': '£13.66',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/vegan-vegetarian-omnivore-dinner-for-everyone-at-the-table_297/index.html'},
     {'title': 'Unstuffed: Decluttering Your Home, Mind, and Soul',
      'price': '£58.09',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/unstuffed-decluttering-your-home-mind-and-soul_296/index.html'},
     {'title': 'Under the Banner of Heaven: A Story of Violent Faith',
      'price': '£30.00',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/under-the-banner-of-heaven-a-story-of-violent-faith_295/index.html'},
     {'title': 'Two Boys Kissing',
      'price': '£32.74',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/two-boys-kissing_294/index.html'},
     {'title': 'Twilight (Twilight #1)',
      'price': '£41.93',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/twilight-twilight-1_293/index.html'},
     {'title': 'Twenties Girl',
      'price': '£42.80',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/twenties-girl_292/index.html'},
     {'title': "Trespassing Across America: One Man's Epic, Never-Done-Before (and Sort of Illegal) Hike Across the Heartland",
      'price': '£53.51',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/trespassing-across-america-one-mans-epic-never-done-before-and-sort-of-illegal-hike-across-the-heartland_291/index.html'},
     {'title': 'Three-Martini Lunch',
      'price': '£23.21',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/three-martini-lunch_290/index.html'},
     {'title': 'Thinking, Fast and Slow',
      'price': '£21.14',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/thinking-fast-and-slow_289/index.html'},
     {'title': 'The Wild Robot',
      'price': '£56.07',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-wild-robot_288/index.html'},
     {'title': 'The Wicked + The Divine, Vol. 3: Commercial Suicide (The Wicked + The Divine)',
      'price': '£14.41',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-wicked-the-divine-vol-3-commercial-suicide-the-wicked-the-divine_287/index.html'},
     {'title': 'The Undomestic Goddess',
      'price': '£45.75',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-undomestic-goddess_286/index.html'},
     {'title': 'The Travelers',
      'price': '£15.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-travelers_285/index.html'},
     {'title': 'The Tipping Point: How Little Things Can Make a Big Difference',
      'price': '£10.02',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-tipping-point-how-little-things-can-make-a-big-difference_284/index.html'},
     {'title': 'The Thing About Jellyfish',
      'price': '£48.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-thing-about-jellyfish_283/index.html'},
     {'title': 'The Stand',
      'price': '£57.86',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-stand_282/index.html'},
     {'title': 'The Smitten Kitchen Cookbook',
      'price': '£23.59',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-smitten-kitchen-cookbook_281/index.html'},
     {'title': 'The Silkworm (Cormoran Strike #2)',
      'price': '£23.05',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-silkworm-cormoran-strike-2_280/index.html'},
     {'title': 'The Sandman, Vol. 3: Dream Country (The Sandman (volumes) #3)',
      'price': '£55.55',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-sandman-vol-3-dream-country-the-sandman-volumes-3_279/index.html'},
     {'title': 'The Rose & the Dagger (The Wrath and the Dawn #2)',
      'price': '£58.64',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-rose-the-dagger-the-wrath-and-the-dawn-2_278/index.html'},
     {'title': 'The Road to Little Dribbling: Adventures of an American in Britain (Notes From a Small Island #2)',
      'price': '£23.21',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-road-to-little-dribbling-adventures-of-an-american-in-britain-notes-from-a-small-island-2_277/index.html'},
     {'title': 'The Rise of Theodore Roosevelt (Theodore Roosevelt #1)',
      'price': '£42.57',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-rise-of-theodore-roosevelt-theodore-roosevelt-1_276/index.html'},
     {'title': "The Restaurant at the End of the Universe (Hitchhiker's Guide to the Galaxy #2)",
      'price': '£10.92',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-restaurant-at-the-end-of-the-universe-hitchhikers-guide-to-the-galaxy-2_275/index.html'},
     {'title': 'The Rest Is Noise: Listening to the Twentieth Century',
      'price': '£34.77',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-rest-is-noise-listening-to-the-twentieth-century_274/index.html'},
     {'title': 'The Red Tent',
      'price': '£35.66',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-red-tent_273/index.html'},
     {'title': 'The Purpose Driven Life: What on Earth Am I Here for?',
      'price': '£37.19',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-purpose-driven-life-what-on-earth-am-i-here-for_272/index.html'},
     {'title': 'The Purest Hook (Second Circle Tattoos #3)',
      'price': '£12.25',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-purest-hook-second-circle-tattoos-3_271/index.html'},
     {'title': 'The Picture of Dorian Gray',
      'price': '£29.70',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-picture-of-dorian-gray_270/index.html'},
     {'title': 'The Paris Wife',
      'price': '£36.80',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-paris-wife_269/index.html'},
     {'title': 'The Obsession',
      'price': '£45.43',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-obsession_268/index.html'},
     {'title': 'The Nightingale',
      'price': '£26.26',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-nightingale_267/index.html'},
     {'title': 'The New Guy (and Other Senior Year Distractions)',
      'price': '£44.92',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-new-guy-and-other-senior-year-distractions_266/index.html'},
     {'title': 'The Nanny Diaries (Nanny #1)',
      'price': '£52.53',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-nanny-diaries-nanny-1_265/index.html'},
     {'title': 'The Name of God is Mercy',
      'price': '£37.25',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-name-of-god-is-mercy_264/index.html'},
     {'title': 'The Maze Runner (The Maze Runner #1)',
      'price': '£20.93',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-maze-runner-the-maze-runner-1_263/index.html'},
     {'title': "The Lover's Dictionary",
      'price': '£58.09',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-lovers-dictionary_262/index.html'},
     {'title': 'The Lonely Ones',
      'price': '£43.59',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-lonely-ones_261/index.html'},
     {'title': "The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses",
      'price': '£33.92',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-lean-startup-how-todays-entrepreneurs-use-continuous-innovation-to-create-radically-successful-businesses_260/index.html'},
     {'title': 'The Last Painting of Sara de Vos',
      'price': '£55.55',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-last-painting-of-sara-de-vos_259/index.html'},
     {'title': 'The Land of 10,000 Madonnas',
      'price': '£29.64',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-land-of-10000-madonnas_258/index.html'},
     {'title': 'The Infinities',
      'price': '£27.41',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-infinities_257/index.html'},
     {'title': "The Husband's Secret",
      'price': '£52.51',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-husbands-secret_256/index.html'},
     {'title': "The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy #1)",
      'price': '£47.80',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-hitchhikers-guide-to-the-galaxy-hitchhikers-guide-to-the-galaxy-1_255/index.html'},
     {'title': 'The Guns of August',
      'price': '£14.54',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-guns-of-august_254/index.html'},
     {'title': 'The Guernsey Literary and Potato Peel Pie Society',
      'price': '£49.53',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-guernsey-literary-and-potato-peel-pie-society_253/index.html'},
     {'title': 'The Goldfinch',
      'price': '£43.58',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-goldfinch_252/index.html'},
     {'title': 'The Giver (The Giver Quartet #1)',
      'price': '£12.30',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-giver-the-giver-quartet-1_251/index.html'},
     {'title': 'The Girl with All the Gifts',
      'price': '£49.47',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-girl-with-all-the-gifts_250/index.html'},
     {'title': 'The Girl Who Played with Fire (Millennium Trilogy #2)',
      'price': '£22.14',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-girl-who-played-with-fire-millennium-trilogy-2_249/index.html'},
     {'title': "The Girl Who Kicked the Hornet's Nest (Millennium Trilogy #3)",
      'price': '£57.48',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-girl-who-kicked-the-hornets-nest-millennium-trilogy-3_248/index.html'},
     {'title': 'The Exiled',
      'price': '£43.45',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-exiled_247/index.html'},
     {'title': 'The End of Faith: Religion, Terror, and the Future of Reason',
      'price': '£22.13',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-end-of-faith-religion-terror-and-the-future-of-reason_246/index.html'},
     {'title': 'The Elegant Universe: Superstrings, Hidden Dimensions, and the Quest for the Ultimate Theory',
      'price': '£13.03',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-elegant-universe-superstrings-hidden-dimensions-and-the-quest-for-the-ultimate-theory_245/index.html'},
     {'title': 'The Disappearing Spoon: And Other True Tales of Madness, Love, and the History of the World from the Periodic Table of the Elements',
      'price': '£57.35',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-disappearing-spoon-and-other-true-tales-of-madness-love-and-the-history-of-the-world-from-the-periodic-table-of-the-elements_244/index.html'},
     {'title': 'The Devil Wears Prada (The Devil Wears Prada #1)',
      'price': '£44.29',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-devil-wears-prada-the-devil-wears-prada-1_243/index.html'},
     {'title': 'The Demon-Haunted World: Science as a Candle in the Dark',
      'price': '£52.25',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-demon-haunted-world-science-as-a-candle-in-the-dark_242/index.html'},
     {'title': 'The Day the Crayons Came Home (Crayons)',
      'price': '£26.33',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-day-the-crayons-came-home-crayons_241/index.html'},
     {'title': 'The Da Vinci Code (Robert Langdon #2)',
      'price': '£22.96',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-da-vinci-code-robert-langdon-2_240/index.html'},
     {'title': "The Cuckoo's Calling (Cormoran Strike #1)",
      'price': '£19.21',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-cuckoos-calling-cormoran-strike-1_239/index.html'},
     {'title': 'The Complete Stories and Poems (The Works of Edgar Allan Poe [Cameo Edition])',
      'price': '£26.78',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-complete-stories-and-poems-the-works-of-edgar-allan-poe-cameo-edition_238/index.html'},
     {'title': 'The Complete Poems',
      'price': '£41.32',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-complete-poems_237/index.html'},
     {'title': 'The Catcher in the Rye',
      'price': '£24.55',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-catcher-in-the-rye_236/index.html'},
     {'title': 'The Cat in the Hat (Beginner Books B-1)',
      'price': '£16.26',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-cat-in-the-hat-beginner-books-b-1_235/index.html'},
     {'title': 'The Case for Christ (Cases for Christianity)',
      'price': '£47.84',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-case-for-christ-cases-for-christianity_234/index.html'},
     {'title': 'The Book Thief',
      'price': '£53.49',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-book-thief_233/index.html'},
     {'title': 'The Book of Basketball: The NBA According to The Sports Guy',
      'price': '£44.84',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-book-of-basketball-the-nba-according-to-the-sports-guy_232/index.html'},
     {'title': 'The Blind Side: Evolution of a Game',
      'price': '£53.71',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-blind-side-evolution-of-a-game_231/index.html'},
     {'title': 'The Autobiography of Malcolm X',
      'price': '£23.43',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-autobiography-of-malcolm-x_230/index.html'},
     {'title': 'The Art of Simple Food: Notes, Lessons, and Recipes from a Delicious Revolution',
      'price': '£34.32',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-art-of-simple-food-notes-lessons-and-recipes-from-a-delicious-revolution_229/index.html'},
     {'title': 'The Art of Fielding',
      'price': '£22.10',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-art-of-fielding_228/index.html'},
     {'title': "Surely You're Joking, Mr. Feynman!: Adventures of a Curious Character",
      'price': '£25.83',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/surely-youre-joking-mr-feynman-adventures-of-a-curious-character_227/index.html'},
     {'title': 'Stiff: The Curious Lives of Human Cadavers',
      'price': '£36.74',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/stiff-the-curious-lives-of-human-cadavers_226/index.html'},
     {'title': 'Spilled Milk: Based on a True Story',
      'price': '£49.51',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/spilled-milk-based-on-a-true-story_225/index.html'},
     {'title': 'Something Borrowed (Darcy & Rachel #1)',
      'price': '£48.96',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/something-borrowed-darcy-rachel-1_224/index.html'},
     {'title': 'Something Blue (Darcy & Rachel #2)',
      'price': '£54.62',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/something-blue-darcy-rachel-2_223/index.html'},
     {'title': 'Soldier (Talon #3)',
      'price': '£24.72',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/soldier-talon-3_222/index.html'},
     {'title': 'Shopaholic & Baby (Shopaholic #5)',
      'price': '£46.45',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/shopaholic-baby-shopaholic-5_221/index.html'},
     {'title': 'Seven Days in the Art World',
      'price': '£52.33',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/seven-days-in-the-art-world_220/index.html'},
     {'title': 'Seven Brief Lessons on Physics',
      'price': '£30.60',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/seven-brief-lessons-on-physics_219/index.html'},
     {'title': 'Scarlet (The Lunar Chronicles #2)',
      'price': '£14.57',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/scarlet-the-lunar-chronicles-2_218/index.html'},
     {'title': "Sarah's Key",
      'price': '£46.29',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/sarahs-key_217/index.html'},
     {'title': 'Saga, Volume 3 (Saga (Collected Editions) #3)',
      'price': '£21.57',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/saga-volume-3-saga-collected-editions-3_216/index.html'},
     {'title': 'Running with Scissors',
      'price': '£12.91',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/running-with-scissors_215/index.html'},
     {'title': 'Rogue Lawyer (Rogue Lawyer #1)',
      'price': '£50.11',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/rogue-lawyer-rogue-lawyer-1_214/index.html'},
     {'title': 'Rise of the Rocket Girls: The Women Who Propelled Us, from Missiles to the Moon to Mars',
      'price': '£41.67',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/rise-of-the-rocket-girls-the-women-who-propelled-us-from-missiles-to-the-moon-to-mars_213/index.html'},
     {'title': 'Rework',
      'price': '£44.88',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/rework_212/index.html'},
     {'title': 'Reservations for Two',
      'price': '£11.10',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/reservations-for-two_211/index.html'},
     {'title': 'Red: The True Story of Red Riding Hood',
      'price': '£28.54',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/red-the-true-story-of-red-riding-hood_210/index.html'},
     {'title': 'Ready Player One',
      'price': '£19.07',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/ready-player-one_209/index.html'},
     {'title': "Quiet: The Power of Introverts in a World That Can't Stop Talking",
      'price': '£43.55',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/quiet-the-power-of-introverts-in-a-world-that-cant-stop-talking_208/index.html'},
     {'title': 'Prodigy: The Graphic Novel (Legend: The Graphic Novel #2)',
      'price': '£43.63',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/prodigy-the-graphic-novel-legend-the-graphic-novel-2_207/index.html'},
     {'title': 'Persepolis: The Story of a Childhood (Persepolis #1-2)',
      'price': '£39.13',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/persepolis-the-story-of-a-childhood-persepolis-1-2_206/index.html'},
     {'title': 'Packing for Mars: The Curious Science of Life in the Void',
      'price': '£56.68',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/packing-for-mars-the-curious-science-of-life-in-the-void_205/index.html'},
     {'title': 'Outliers: The Story of Success',
      'price': '£14.16',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/outliers-the-story-of-success_204/index.html'},
     {'title': 'Original Fake',
      'price': '£31.45',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/original-fake_203/index.html'},
     {'title': 'Orange Is the New Black',
      'price': '£24.61',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/orange-is-the-new-black_202/index.html'},
     {'title': 'One for the Money (Stephanie Plum #1)',
      'price': '£32.87',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/one-for-the-money-stephanie-plum-1_201/index.html'},
     {'title': 'Notes from a Small Island (Notes From a Small Island #1)',
      'price': '£40.17',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/notes-from-a-small-island-notes-from-a-small-island-1_200/index.html'},
     {'title': 'Night (The Night Trilogy #1)',
      'price': '£13.51',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/night-the-night-trilogy-1_199/index.html'},
     {'title': 'Neither Here nor There: Travels in Europe',
      'price': '£38.95',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/neither-here-nor-there-travels-in-europe_198/index.html'},
     {'title': 'Naked',
      'price': '£31.69',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/naked_197/index.html'},
     {'title': 'Morning Star (Red Rising #3)',
      'price': '£29.40',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/morning-star-red-rising-3_196/index.html'},
     {'title': 'Miracles from Heaven: A Little Girl, Her Journey to Heaven, and Her Amazing Story of Healing',
      'price': '£57.83',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/miracles-from-heaven-a-little-girl-her-journey-to-heaven-and-her-amazing-story-of-healing_195/index.html'},
     {'title': 'Midnight Riot (Peter Grant/ Rivers of London - books #1)',
      'price': '£55.46',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/midnight-riot-peter-grant-rivers-of-london-books-1_194/index.html'},
     {'title': 'Me Talk Pretty One Day',
      'price': '£57.60',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/me-talk-pretty-one-day_193/index.html'},
     {'title': 'Manuscript Found in Accra',
      'price': '£34.98',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/manuscript-found-in-accra_192/index.html'},
     {'title': 'Lust & Wonder',
      'price': '£11.87',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/lust-wonder_191/index.html'},
     {'title': 'Lila (Gilead #3)',
      'price': '£12.47',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/lila-gilead-3_190/index.html'},
     {'title': "Life, the Universe and Everything (Hitchhiker's Guide to the Galaxy #3)",
      'price': '£33.26',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/life-the-universe-and-everything-hitchhikers-guide-to-the-galaxy-3_189/index.html'},
     {'title': 'Life Without a Recipe',
      'price': '£59.04',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/life-without-a-recipe_188/index.html'},
     {'title': 'Life After Life',
      'price': '£26.13',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/life-after-life_187/index.html'},
     {'title': 'Letter to a Christian Nation',
      'price': '£22.20',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/letter-to-a-christian-nation_186/index.html'},
     {'title': "Let's Pretend This Never Happened: A Mostly True Memoir",
      'price': '£45.11',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/lets-pretend-this-never-happened-a-mostly-true-memoir_185/index.html'},
     {'title': 'Legend (Legend #1)',
      'price': '£43.69',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/legend-legend-1_184/index.html'},
     {'title': 'Lean In: Women, Work, and the Will to Lead',
      'price': '£25.02',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/lean-in-women-work-and-the-will-to-lead_183/index.html'},
     {'title': "Lamb: The Gospel According to Biff, Christ's Childhood Pal",
      'price': '£55.50',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/lamb-the-gospel-according-to-biff-christs-childhood-pal_182/index.html'},
     {'title': 'Lady Renegades (Rebel Belle #3)',
      'price': '£53.04',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/lady-renegades-rebel-belle-3_181/index.html'},
     {'title': 'Jurassic Park (Jurassic Park #1)',
      'price': '£44.97',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/jurassic-park-jurassic-park-1_180/index.html'},
     {'title': "It's Never Too Late to Begin Again: Discovering Creativity and Meaning at Midlife and Beyond",
      'price': '£42.38',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/its-never-too-late-to-begin-again-discovering-creativity-and-meaning-at-midlife-and-beyond_179/index.html'},
     {'title': 'Is Everyone Hanging Out Without Me? (And Other Concerns)',
      'price': '£20.11',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/is-everyone-hanging-out-without-me-and-other-concerns_178/index.html'},
     {'title': 'Into the Wild',
      'price': '£56.70',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/into-the-wild_177/index.html'},
     {'title': 'Inferno (Robert Langdon #4)',
      'price': '£41.00',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/inferno-robert-langdon-4_176/index.html'},
     {'title': "In the Garden of Beasts: Love, Terror, and an American Family in Hitler's Berlin",
      'price': '£28.85',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/in-the-garden-of-beasts-love-terror-and-an-american-family-in-hitlers-berlin_175/index.html'},
     {'title': 'If I Run (If I Run #1)',
      'price': '£49.97',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/if-i-run-if-i-run-1_174/index.html'},
     {'title': "I've Got Your Number",
      'price': '£19.69',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/ive-got-your-number_173/index.html'},
     {'title': 'I Am Malala: The Girl Who Stood Up for Education and Was Shot by the Taliban',
      'price': '£28.88',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/i-am-malala-the-girl-who-stood-up-for-education-and-was-shot-by-the-taliban_172/index.html'},
     {'title': 'Hungry Girl Clean & Hungry: Easy All-Natural Recipes for Healthy Eating in the Real World',
      'price': '£33.14',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/hungry-girl-clean-hungry-easy-all-natural-recipes-for-healthy-eating-in-the-real-world_171/index.html'},
     {'title': 'House of Lost Worlds: Dinosaurs, Dynasties, and the Story of Life on Earth',
      'price': '£43.70',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/house-of-lost-worlds-dinosaurs-dynasties-and-the-story-of-life-on-earth_170/index.html'},
     {'title': 'House of Leaves',
      'price': '£54.89',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/house-of-leaves_169/index.html'},
     {'title': 'Horrible Bear!',
      'price': '£37.52',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/horrible-bear_168/index.html'},
     {'title': 'Holidays on Ice',
      'price': '£51.07',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/holidays-on-ice_167/index.html'},
     {'title': 'Heir to the Sky',
      'price': '£44.07',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/heir-to-the-sky_166/index.html'},
     {'title': 'Green Eggs and Ham (Beginner Books B-16)',
      'price': '£10.79',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/green-eggs-and-ham-beginner-books-b-16_165/index.html'},
     {'title': 'Grayson, Vol 3: Nemesis (Grayson #3)',
      'price': '£42.72',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/grayson-vol-3-nemesis-grayson-3_164/index.html'},
     {'title': 'Gratitude',
      'price': '£26.66',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/gratitude_163/index.html'},
     {'title': 'Gone Girl',
      'price': '£37.60',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/gone-girl_162/index.html'},
     {'title': 'Golden (Heart of Dread #3)',
      'price': '£42.21',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/golden-heart-of-dread-3_161/index.html'},
     {'title': 'Girl in the Blue Coat',
      'price': '£46.83',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/girl-in-the-blue-coat_160/index.html'},
     {'title': 'Fruits Basket, Vol. 3 (Fruits Basket #3)',
      'price': '£45.17',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/fruits-basket-vol-3-fruits-basket-3_159/index.html'},
     {'title': 'Friday Night Lights: A Town, a Team, and a Dream',
      'price': '£51.22',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/friday-night-lights-a-town-a-team-and-a-dream_158/index.html'},
     {'title': 'Fire Bound (Sea Haven/Sisters of the Heart #5)',
      'price': '£21.28',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/fire-bound-sea-havensisters-of-the-heart-5_157/index.html'},
     {'title': 'Fifty Shades Freed (Fifty Shades #3)',
      'price': '£15.36',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/fifty-shades-freed-fifty-shades-3_156/index.html'},
     {'title': 'Fellside',
      'price': '£38.62',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/fellside_155/index.html'},
     {'title': 'Extreme Prey (Lucas Davenport #26)',
      'price': '£25.40',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/extreme-prey-lucas-davenport-26_154/index.html'},
     {'title': 'Eragon (The Inheritance Cycle #1)',
      'price': '£43.87',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/eragon-the-inheritance-cycle-1_153/index.html'},
     {'title': 'Eclipse (Twilight #3)',
      'price': '£18.74',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/eclipse-twilight-3_152/index.html'},
     {'title': 'Dune (Dune #1)',
      'price': '£54.86',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/dune-dune-1_151/index.html'},
     {'title': 'Dracula',
      'price': '£52.62',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/dracula_150/index.html'},
     {'title': 'Do Androids Dream of Electric Sheep? (Blade Runner #1)',
      'price': '£51.48',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/do-androids-dream-of-electric-sheep-blade-runner-1_149/index.html'},
     {'title': 'Disrupted: My Misadventure in the Start-Up Bubble',
      'price': '£15.28',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/disrupted-my-misadventure-in-the-start-up-bubble_148/index.html'},
     {'title': 'Dead Wake: The Last Crossing of the Lusitania',
      'price': '£39.24',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/dead-wake-the-last-crossing-of-the-lusitania_147/index.html'},
     {'title': 'David and Goliath: Underdogs, Misfits, and the Art of Battling Giants',
      'price': '£17.81',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/david-and-goliath-underdogs-misfits-and-the-art-of-battling-giants_146/index.html'},
     {'title': 'Darkfever (Fever #1)',
      'price': '£56.02',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/darkfever-fever-1_145/index.html'},
     {'title': 'Dark Places',
      'price': '£23.90',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/dark-places_144/index.html'},
     {'title': 'Crazy Rich Asians (Crazy Rich Asians #1)',
      'price': '£49.13',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/crazy-rich-asians-crazy-rich-asians-1_143/index.html'},
     {'title': 'Counting Thyme',
      'price': '£10.62',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/counting-thyme_142/index.html'},
     {'title': 'Cosmos',
      'price': '£36.17',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/cosmos_141/index.html'},
     {'title': 'Civilization and Its Discontents',
      'price': '£59.95',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/civilization-and-its-discontents_140/index.html'},
     {'title': 'Cinder (The Lunar Chronicles #1)',
      'price': '£26.09',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/cinder-the-lunar-chronicles-1_139/index.html'},
     {'title': "Catastrophic Happiness: Finding Joy in Childhood's Messy Years",
      'price': '£37.35',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/catastrophic-happiness-finding-joy-in-childhoods-messy-years_138/index.html'},
     {'title': 'Career of Evil (Cormoran Strike #3)',
      'price': '£24.72',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/career-of-evil-cormoran-strike-3_137/index.html'},
     {'title': 'Breaking Dawn (Twilight #4)',
      'price': '£35.28',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/breaking-dawn-twilight-4_136/index.html'},
     {'title': 'Brave Enough',
      'price': '£51.32',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/brave-enough_135/index.html'},
     {'title': 'Boy Meets Boy',
      'price': '£21.12',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/boy-meets-boy_134/index.html'},
     {'title': 'Born to Run: A Hidden Tribe, Superathletes, and the Greatest Race the World Has Never Seen',
      'price': '£27.35',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/born-to-run-a-hidden-tribe-superathletes-and-the-greatest-race-the-world-has-never-seen_133/index.html'},
     {'title': 'Blink: The Power of Thinking Without Thinking',
      'price': '£21.74',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/blink-the-power-of-thinking-without-thinking_132/index.html'},
     {'title': 'Black Flags: The Rise of ISIS',
      'price': '£40.87',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/black-flags-the-rise-of-isis_131/index.html'},
     {'title': 'Black Butler, Vol. 1 (Black Butler #1)',
      'price': '£49.31',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/black-butler-vol-1-black-butler-1_130/index.html'},
     {'title': 'Big Little Lies',
      'price': '£22.11',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/big-little-lies_129/index.html'},
     {'title': 'Between Shades of Gray',
      'price': '£20.79',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/between-shades-of-gray_128/index.html'},
     {'title': "Best of My Love (Fool's Gold #20)",
      'price': '£27.41',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/best-of-my-love-fools-gold-20_127/index.html'},
     {'title': 'Beowulf',
      'price': '£38.35',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/beowulf_126/index.html'},
     {'title': 'Beautiful Creatures (Caster Chronicles #1)',
      'price': '£21.55',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/beautiful-creatures-caster-chronicles-1_125/index.html'},
     {'title': 'Awkward',
      'price': '£38.02',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/awkward_124/index.html'},
     {'title': 'Ash',
      'price': '£22.06',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/ash_123/index.html'},
     {'title': 'Are We There Yet?',
      'price': '£10.66',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/are-we-there-yet_122/index.html'},
     {'title': 'Are We Smart Enough to Know How Smart Animals Are?',
      'price': '£56.58',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/are-we-smart-enough-to-know-how-smart-animals-are_121/index.html'},
     {'title': 'Annie on My Mind',
      'price': '£36.83',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/annie-on-my-mind_120/index.html'},
     {'title': 'And Then There Were None',
      'price': '£35.01',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/and-then-there-were-none_119/index.html'},
     {'title': 'A Walk in the Woods: Rediscovering America on the Appalachian Trail',
      'price': '£30.48',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/a-walk-in-the-woods-rediscovering-america-on-the-appalachian-trail_118/index.html'},
     {'title': 'A Visit from the Goon Squad',
      'price': '£14.08',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/a-visit-from-the-goon-squad_117/index.html'},
     {'title': 'A Storm of Swords (A Song of Ice and Fire #3)',
      'price': '£31.22',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/a-storm-of-swords-a-song-of-ice-and-fire-3_116/index.html'},
     {'title': 'A Heartbreaking Work of Staggering Genius',
      'price': '£54.29',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/a-heartbreaking-work-of-staggering-genius_115/index.html'},
     {'title': '8 Keys to Mental Health Through Exercise',
      'price': '£31.04',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/8-keys-to-mental-health-through-exercise_114/index.html'},
     {'title': '#GIRLBOSS',
      'price': '£50.96',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/girlboss_113/index.html'},
     {'title': 'The Suffragettes (Little Black Classics, #96)',
      'price': '£11.89',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-suffragettes-little-black-classics-96_112/index.html'},
     {'title': 'The Sense of an Ending',
      'price': '£31.38',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-sense-of-an-ending_111/index.html'},
     {'title': "The Sandman, Vol. 2: The Doll's House (The Sandman (volumes) #2)",
      'price': '£54.81',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-sandman-vol-2-the-dolls-house-the-sandman-volumes-2_110/index.html'},
     {'title': 'The Course of Love',
      'price': '£16.78',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-course-of-love_109/index.html'},
     {'title': 'Sugar Rush (Offensive Line #2)',
      'price': '£24.42',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/sugar-rush-offensive-line-2_108/index.html'},
     {'title': 'Saga, Volume 2 (Saga (Collected Editions) #2)',
      'price': '£11.75',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/saga-volume-2-saga-collected-editions-2_107/index.html'},
     {'title': 'Run, Spot, Run: The Ethics of Keeping Pets',
      'price': '£20.02',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/run-spot-run-the-ethics-of-keeping-pets_106/index.html'},
     {'title': 'New Moon (Twilight #2)',
      'price': '£12.86',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/new-moon-twilight-2_105/index.html'},
     {'title': 'Life',
      'price': '£31.58',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/life_104/index.html'},
     {'title': "Kindle Paperwhite User's Guide",
      'price': '£34.00',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/kindle-paperwhite-users-guide_103/index.html'},
     {'title': 'H is for Hawk',
      'price': '£57.42',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/h-is-for-hawk_102/index.html'},
     {'title': 'Girl Online On Tour (Girl Online #2)',
      'price': '£53.47',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/girl-online-on-tour-girl-online-2_101/index.html'},
     {'title': 'Fruits Basket, Vol. 2 (Fruits Basket #2)',
      'price': '£11.64',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/fruits-basket-vol-2-fruits-basket-2_100/index.html'},
     {'title': 'Diary of a Minecraft Zombie Book 1: A Scare of a Dare (An Unofficial Minecraft Book)',
      'price': '£52.88',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/diary-of-a-minecraft-zombie-book-1-a-scare-of-a-dare-an-unofficial-minecraft-book_99/index.html'},
     {'title': 'Y: The Last Man, Vol. 1: Unmanned (Y: The Last Man #1)',
      'price': '£18.51',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/y-the-last-man-vol-1-unmanned-y-the-last-man-1_98/index.html'},
     {'title': 'While You Were Mine',
      'price': '£41.32',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/while-you-were-mine_97/index.html'},
     {'title': 'Where Lightning Strikes (Bleeding Stars #3)',
      'price': '£39.77',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/where-lightning-strikes-bleeding-stars-3_96/index.html'},
     {'title': "When I'm Gone",
      'price': '£51.96',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/when-im-gone_95/index.html'},
     {'title': 'Ways of Seeing',
      'price': '£39.51',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/ways-of-seeing_94/index.html'},
     {'title': 'Vampire Knight, Vol. 1 (Vampire Knight #1)',
      'price': '£15.40',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/vampire-knight-vol-1-vampire-knight-1_93/index.html'},
     {'title': 'Vampire Girl (Vampire Girl #1)',
      'price': '£53.82',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/vampire-girl-vampire-girl-1_92/index.html'},
     {'title': 'Twenty Love Poems and a Song of Despair',
      'price': '£30.95',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/twenty-love-poems-and-a-song-of-despair_91/index.html'},
     {'title': 'Travels with Charley: In Search of America',
      'price': '£57.82',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/travels-with-charley-in-search-of-america_90/index.html'},
     {'title': 'Three Wishes (River of Time: California #1)',
      'price': '£44.18',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/three-wishes-river-of-time-california-1_89/index.html'},
     {'title': 'This One Moment (Pushing Limits #1)',
      'price': '£48.71',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/this-one-moment-pushing-limits-1_88/index.html'},
     {'title': 'The Zombie Room',
      'price': '£19.69',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-zombie-room_87/index.html'},
     {'title': 'The Wicked + The Divine, Vol. 1: The Faust Act (The Wicked + The Divine)',
      'price': '£36.52',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-wicked-the-divine-vol-1-the-faust-act-the-wicked-the-divine_86/index.html'},
     {'title': 'The Tumor',
      'price': '£41.56',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-tumor_85/index.html'},
     {'title': 'The Story of Hong Gildong',
      'price': '£43.19',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-story-of-hong-gildong_84/index.html'},
     {'title': 'The Silent Wife',
      'price': '£12.34',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-silent-wife_83/index.html'},
     {'title': 'The Silent Twin (Detective Jennifer Knight #3)',
      'price': '£36.25',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-silent-twin-detective-jennifer-knight-3_82/index.html'},
     {'title': 'The Selfish Gene',
      'price': '£29.45',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-selfish-gene_81/index.html'},
     {'title': 'The Secret Healer',
      'price': '£34.56',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-secret-healer_80/index.html'},
     {'title': 'The Sandman, Vol. 1: Preludes and Nocturnes (The Sandman (volumes) #1)',
      'price': '£54.12',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-sandman-vol-1-preludes-and-nocturnes-the-sandman-volumes-1_79/index.html'},
     {'title': 'The Republic',
      'price': '£33.78',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-republic_78/index.html'},
     {'title': 'The Odyssey',
      'price': '£29.64',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-odyssey_77/index.html'},
     {'title': "The No. 1 Ladies' Detective Agency (No. 1 Ladies' Detective Agency #1)",
      'price': '£57.70',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-no-1-ladies-detective-agency-no-1-ladies-detective-agency-1_76/index.html'},
     {'title': 'The Nicomachean Ethics',
      'price': '£36.34',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-nicomachean-ethics_75/index.html'},
     {'title': 'The Name of the Wind (The Kingkiller Chronicle #1)',
      'price': '£50.59',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-name-of-the-wind-the-kingkiller-chronicle-1_74/index.html'},
     {'title': 'The Mirror & the Maze (The Wrath and the Dawn #1.5)',
      'price': '£29.38',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-mirror-the-maze-the-wrath-and-the-dawn-15_73/index.html'},
     {'title': 'The Little Prince',
      'price': '£45.42',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-little-prince_72/index.html'},
     {'title': 'The Light of the Fireflies',
      'price': '£54.43',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-light-of-the-fireflies_71/index.html'},
     {'title': 'The Last Girl (The Dominion Trilogy #1)',
      'price': '£36.26',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/the-last-girl-the-dominion-trilogy-1_70/index.html'},
     {'title': 'The Iliad',
      'price': '£16.16',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-iliad_69/index.html'},
     {'title': 'The Hook Up (Game On #1)',
      'price': '£36.29',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-hook-up-game-on-1_68/index.html'},
     {'title': 'The Haters',
      'price': '£27.89',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-haters_67/index.html'},
     {'title': 'The Girl You Lost',
      'price': '£12.29',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/the-girl-you-lost_66/index.html'},
     {'title': 'The Girl In The Ice (DCI Erika Foster #1)',
      'price': '£15.85',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-girl-in-the-ice-dci-erika-foster-1_65/index.html'},
     {'title': 'The End of the Jesus Era (An Investigation #1)',
      'price': '£14.40',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/the-end-of-the-jesus-era-an-investigation-1_64/index.html'},
     {'title': 'The Edge of Reason (Bridget Jones #2)',
      'price': '£19.18',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-edge-of-reason-bridget-jones-2_63/index.html'},
     {'title': 'The Complete Maus (Maus #1-2)',
      'price': '£10.64',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-complete-maus-maus-1-2_62/index.html'},
     {'title': 'The Communist Manifesto',
      'price': '£14.76',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-communist-manifesto_61/index.html'},
     {'title': 'The Bhagavad Gita',
      'price': '£57.49',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-bhagavad-gita_60/index.html'},
     {'title': 'The Bette Davis Club',
      'price': '£30.66',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/the-bette-davis-club_59/index.html'},
     {'title': 'The Art of Not Breathing',
      'price': '£40.83',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/the-art-of-not-breathing_58/index.html'},
     {'title': 'Taking Shots (Assassins #1)',
      'price': '£18.88',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/taking-shots-assassins-1_57/index.html'},
     {'title': 'Starlark',
      'price': '£25.83',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/starlark_56/index.html'},
     {'title': 'Skip Beat!, Vol. 01 (Skip Beat! #1)',
      'price': '£42.12',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/skip-beat-vol-01-skip-beat-1_55/index.html'},
     {'title': 'Sister Sable (The Mad Queen #1)',
      'price': '£13.33',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/sister-sable-the-mad-queen-1_54/index.html'},
     {'title': 'Shatter Me (Shatter Me #1)',
      'price': '£42.40',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/shatter-me-shatter-me-1_53/index.html'},
     {'title': 'Shameless',
      'price': '£58.35',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/shameless_52/index.html'},
     {'title': 'Shadow Rites (Jane Yellowrock #10)',
      'price': '£21.72',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/shadow-rites-jane-yellowrock-10_51/index.html'},
     {'title': 'Settling the Score (The Summer Games #1)',
      'price': '£44.91',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/settling-the-score-the-summer-games-1_50/index.html'},
     {'title': 'Sense and Sensibility',
      'price': '£37.46',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/sense-and-sensibility_49/index.html'},
     {'title': 'Saga, Volume 1 (Saga (Collected Editions) #1)',
      'price': '£28.48',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/saga-volume-1-saga-collected-editions-1_48/index.html'},
     {'title': 'Rhythm, Chord & Malykhin',
      'price': '£28.34',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/rhythm-chord-malykhin_47/index.html'},
     {'title': 'Rat Queens, Vol. 1: Sass & Sorcery (Rat Queens (Collected Editions) #1-5)',
      'price': '£46.96',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/rat-queens-vol-1-sass-sorcery-rat-queens-collected-editions-1-5_46/index.html'},
     {'title': 'Paradise Lost (Paradise #1)',
      'price': '£24.96',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/paradise-lost-paradise-1_45/index.html'},
     {'title': 'Paper Girls, Vol. 1 (Paper Girls #1-5)',
      'price': '£21.71',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/paper-girls-vol-1-paper-girls-1-5_44/index.html'},
     {'title': 'Ouran High School Host Club, Vol. 1 (Ouran High School Host Club #1)',
      'price': '£29.87',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/ouran-high-school-host-club-vol-1-ouran-high-school-host-club-1_43/index.html'},
     {'title': 'Origins (Alphas 0.5)',
      'price': '£28.99',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/origins-alphas-05_42/index.html'},
     {'title': 'One Second (Seven #7)',
      'price': '£52.94',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/one-second-seven-7_41/index.html'},
     {'title': 'On the Road (Duluoz Legend)',
      'price': '£32.36',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/on-the-road-duluoz-legend_40/index.html'},
     {'title': "Old Records Never Die: One Man's Quest for His Vinyl and His Past",
      'price': '£55.66',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/old-records-never-die-one-mans-quest-for-his-vinyl-and-his-past_39/index.html'},
     {'title': 'Off Sides (Off #1)',
      'price': '£39.45',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/off-sides-off-1_38/index.html'},
     {'title': 'Of Mice and Men',
      'price': '£47.11',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/of-mice-and-men_37/index.html'},
     {'title': 'Myriad (Prentor #1)',
      'price': '£58.75',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/myriad-prentor-1_36/index.html'},
     {'title': 'My Perfect Mistake (Over the Top #1)',
      'price': '£38.92',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/my-perfect-mistake-over-the-top-1_35/index.html'},
     {'title': 'Ms. Marvel, Vol. 1: No Normal (Ms. Marvel (2014-2015) #1)',
      'price': '£39.39',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/ms-marvel-vol-1-no-normal-ms-marvel-2014-2015-1_34/index.html'},
     {'title': 'Meditations',
      'price': '£25.89',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/meditations_33/index.html'},
     {'title': 'Matilda',
      'price': '£28.34',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/matilda_32/index.html'},
     {'title': 'Lost Among the Living',
      'price': '£27.70',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/lost-among-the-living_31/index.html'},
     {'title': 'Lord of the Flies',
      'price': '£24.89',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/lord-of-the-flies_30/index.html'},
     {'title': 'Listen to Me (Fusion #1)',
      'price': '£58.99',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/listen-to-me-fusion-1_29/index.html'},
     {'title': 'Kitchens of the Great Midwest',
      'price': '£57.20',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/kitchens-of-the-great-midwest_28/index.html'},
     {'title': 'Jane Eyre',
      'price': '£38.43',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/jane-eyre_27/index.html'},
     {'title': 'Imperfect Harmony',
      'price': '£34.74',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/imperfect-harmony_26/index.html'},
     {'title': 'Icing (Aces Hockey #2)',
      'price': '£40.44',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/icing-aces-hockey-2_25/index.html'},
     {'title': 'Hawkeye, Vol. 1: My Life as a Weapon (Hawkeye #1)',
      'price': '£45.24',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/hawkeye-vol-1-my-life-as-a-weapon-hawkeye-1_24/index.html'},
     {'title': "Having the Barbarian's Baby (Ice Planet Barbarians #7.5)",
      'price': '£34.96',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/having-the-barbarians-baby-ice-planet-barbarians-75_23/index.html'},
     {'title': 'Giant Days, Vol. 1 (Giant Days #1-4)',
      'price': '£56.76',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/giant-days-vol-1-giant-days-1-4_22/index.html'},
     {'title': 'Fruits Basket, Vol. 1 (Fruits Basket #1)',
      'price': '£40.28',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/fruits-basket-vol-1-fruits-basket-1_21/index.html'},
     {'title': 'Frankenstein',
      'price': '£38.00',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/frankenstein_20/index.html'},
     {'title': 'Forever Rockers (The Rocker #12)',
      'price': '£28.80',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/forever-rockers-the-rocker-12_19/index.html'},
     {'title': 'Fighting Fate (Fighting #6)',
      'price': '£39.24',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/fighting-fate-fighting-6_18/index.html'},
     {'title': 'Emma',
      'price': '£32.93',
      'instock': True,
      'stars': 'Two',
      'url': 'http://books.toscrape.com/emma_17/index.html'},
     {'title': 'Eat, Pray, Love',
      'price': '£51.32',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/eat-pray-love_16/index.html'},
     {'title': 'Deep Under (Walker Security #1)',
      'price': '£47.09',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/deep-under-walker-security-1_15/index.html'},
     {'title': "Choosing Our Religion: The Spiritual Lives of America's Nones",
      'price': '£28.42',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/choosing-our-religion-the-spiritual-lives-of-americas-nones_14/index.html'},
     {'title': 'Charlie and the Chocolate Factory (Charlie Bucket #1)',
      'price': '£22.85',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/charlie-and-the-chocolate-factory-charlie-bucket-1_13/index.html'},
     {'title': "Charity's Cross (Charles Towne Belles #4)",
      'price': '£41.24',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/charitys-cross-charles-towne-belles-4_12/index.html'},
     {'title': 'Bright Lines',
      'price': '£39.07',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/bright-lines_11/index.html'},
     {'title': "Bridget Jones's Diary (Bridget Jones #1)",
      'price': '£29.82',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/bridget-joness-diary-bridget-jones-1_10/index.html'},
     {'title': 'Bounty (Colorado Mountain #7)',
      'price': '£37.26',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/bounty-colorado-mountain-7_9/index.html'},
     {'title': 'Blood Defense (Samantha Brinkman #1)',
      'price': '£20.30',
      'instock': True,
      'stars': 'Three',
      'url': 'http://books.toscrape.com/blood-defense-samantha-brinkman-1_8/index.html'},
     {'title': 'Bleach, Vol. 1: Strawberry and the Soul Reapers (Bleach #1)',
      'price': '£34.65',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/bleach-vol-1-strawberry-and-the-soul-reapers-bleach-1_7/index.html'},
     {'title': 'Beyond Good and Evil',
      'price': '£43.38',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/beyond-good-and-evil_6/index.html'},
     {'title': "Alice in Wonderland (Alice's Adventures in Wonderland #1)",
      'price': '£55.53',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/alice-in-wonderland-alices-adventures-in-wonderland-1_5/index.html'},
     {'title': 'Ajin: Demi-Human, Volume 1 (Ajin: Demi-Human #1)',
      'price': '£57.06',
      'instock': True,
      'stars': 'Four',
      'url': 'http://books.toscrape.com/ajin-demi-human-volume-1-ajin-demi-human-1_4/index.html'},
     {'title': "A Spy's Devotion (The Regency Spies of London #1)",
      'price': '£16.97',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/a-spys-devotion-the-regency-spies-of-london-1_3/index.html'},
     {'title': "1st to Die (Women's Murder Club #1)",
      'price': '£53.98',
      'instock': True,
      'stars': 'One',
      'url': 'http://books.toscrape.com/1st-to-die-womens-murder-club-1_2/index.html'},
     {'title': '1,000 Places to See Before You Die',
      'price': '£26.08',
      'instock': True,
      'stars': 'Five',
      'url': 'http://books.toscrape.com/1000-places-to-see-before-you-die_1/index.html'}]




```python
df = pd.DataFrame(all_dicts)

df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>price</th>
      <th>instock</th>
      <th>stars</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A Light in the Attic</td>
      <td>£51.77</td>
      <td>True</td>
      <td>Three</td>
      <td>http://books.toscrape.com/a-light-in-the-attic...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tipping the Velvet</td>
      <td>£53.74</td>
      <td>True</td>
      <td>One</td>
      <td>http://books.toscrape.com/tipping-the-velvet_9...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Soumission</td>
      <td>£50.10</td>
      <td>True</td>
      <td>One</td>
      <td>http://books.toscrape.com/soumission_998/index...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sharp Objects</td>
      <td>£47.82</td>
      <td>True</td>
      <td>Four</td>
      <td>http://books.toscrape.com/sharp-objects_997/in...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sapiens: A Brief History of Humankind</td>
      <td>£54.23</td>
      <td>True</td>
      <td>Five</td>
      <td>http://books.toscrape.com/sapiens-a-brief-hist...</td>
    </tr>
  </tbody>
</table>
</div>



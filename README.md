Note to the Reviewers
----
Clone the repository and fire up the dev server to view the site. Since the database is included in the repo (db.sqlite3) it shouldn't be necessary to intialize it, but you can do so by executing the script `./starter/data/load_data_script.py` from the django shell (`python manage.py shell`) using the `execfile` function.

The site simply displays a list of all movies in the database (without pagination) and allows the user to navigate to a more detailed view of individual movies. A search bar at the top filters movies for exact case-insensitive matches of the search term in the movie title or synopsis. A set of filters on the left can be used to filter movie results on several criteria.

Another approach to the movie list would be use of asynchronous requests and javascript to update the list on the client-side, which generally feels snappier and seems to be what you guys favor in KA Lite. This would require implementing some kind of API, and I chose instead to keep it simple for this exercise.

I spent the most time in this exercise in `starter/models.py`, first in order to make a decision about how to represent the more complex attributes in the dataset, like `ratings`, since Django Models don't have a native dictionary field. I chose to use a package called JSONField (and I added it to `requirements.txt`), which works pretty much how you would expect. The decision to make `ratings` a JSONField and the need to filter querysets on its parsed attributes posed a problem, as a JSONField is stored unparsed in the database. This required me to implement a custom Manager for the Model, and after some reading I chose to implement it such that it simply extends the available QuerySet methods and allows arbitrary chaining. This is in contrast to simpler implementations of Managers that work in parallel to other Managers and do not allow arbitrary chaining. For example, constructions like `Movie.objects.some_custom_filter().some_default_filter().any_arbitrary_queryset_method()` are possible in my implementation.

Michael's Working Notes
----
Possible improvements:
* Pagination on movie list display.
* Better search functionality (allow inexact matches, search on other attributes)
* It would be nice if searching for a term and then filtering worked as expected (it doesn't, but the reverse order does). One way to do that is to keep the search term as a cookie.

Instructions
----

Hi there, and thanks for applying to join the core FLE dev team!
To give you a chance to demonstrate how you approach a problem,
using a variety of technologies and a healthy dose of creative
freedom, we've put together this short practice project. To make
it a bit faster for you to get started, we put together this
skeleton repository that you can use as a starting point.

Within this repository's `starter/data/` folder is a `movies.json`
file, which is a snapshot of the Rotten Tomatoes API. Your task is to
display all the movies (e.g. in a list), and allow the user to view details
of a movie once it's clicked. You can use whatever technologies and
methods you'd like to accomplish this task; the only requirement is to
use Django as the backend web framework. You can also add other features
such as search or filtering, make it a single-page JS app, or focus on
making it pretty, etc.

So to get things started, do the following:

1. Clone this repo into your local machine (DO NOT FORK!)
2. Create a new repository in your github account
3. Change your local repository's origin remote to point to your new remote Github repository
4. Once you're satisfied with your code, push your local repository into the remote Github repository
5. Send us the link to your Github repo!

That's it! We'll review your code soon and get back to you once we're done!

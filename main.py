from requests import get
from bs4 import BeautifulSoup


def get_response():
    """Get response from GET request"""

    url = 'https://www.imdb.com/chart/top'
    response = get(url)
    return response


def parse_data(response):
    """
    Make a list of top rated films in this way:
        Film name | Year | Rating Imdb
    """
    film_list = []

    soup = BeautifulSoup(response.content, 'lxml')
    title_tags = soup(class_='titleColumn')
    rating_tags = soup(class_='imdbRating')

    for title, rating in zip(title_tags, rating_tags):
        name = title.a.string + ' ' + title.span.string
        rate = rating.strong.string

        film_list.append((name, rate))
    
    return film_list

def print_list(film_list):
    """Print the top of films"""

    print('Top Rated Movies by IMDb Users:\n')
    for i, (title, rating) in enumerate(film_list):
        print(str(i + 1) + '.', title, 'Rating IMDb:', rating)


def main():
    response = get_response()
    film_list = parse_data(response)
    print_list(film_list)


main()

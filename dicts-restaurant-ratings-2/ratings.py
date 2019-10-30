"""Restaurant rating lister."""

def parse_file_into_dict(file):

    restaurant_scores = open(file)
    restaurant_score_dict = {}
    
    for restaurant_score in restaurant_scores:
        restaurant_score = restaurant_score.rstrip()
        restaurant_score = restaurant_score.split(':') #split each line to create a list
        restaurant_name = restaurant_score[0]
        restaurant_rating = restaurant_score[1]
        restaurant_score_dict[restaurant_name] = restaurant_rating

    return restaurant_score_dict


def restaurant_ratings(file):
    """Prints restaurant name and rating in alphabetical order"""
    restaurant_score_dict = restaurant_rating_input(file)
    restaurant_score_tuple = sorted(restaurant_score_dict.items())
    
    for restaurant, score in restaurant_score_tuple:
        print(f'{restaurant} is rated at {score}.')



def add_restaurant_rating_input(file):
    restaurant_score_dict = parse_file_into_dict(file)
    restaurant_name = input("What is your restaurant's name? ")
    restaurant_score = input("What is your restaurant's score? ")
    restaurant_score_dict[restaurant_name] = restaurant_score
    return restaurant_score_dict

restaurant_ratings("scores.txt")

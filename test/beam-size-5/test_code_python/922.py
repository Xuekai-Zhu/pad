def solution():
    
    total_money = 150
    friday_tickets = 5
    saturday_tickets = 10
    other_day_tickets = 7
    popcorn_tickets = 8
    candy_boxes = 2
    friday_movies = 5
    saturday_movies = friday_movies + saturday_movies
    other_day_movies = other_day_tickets - friday_movies - saturday_movies
    popcorn_cost = popcorn_tickets * candy_boxes
    candy_cost = candy_boxes * candy_boxes
    total_movies = friday_movies + saturday_movies + other_day_movies + popcorn_cost + candy_cost
    result = total_movies
    return result

print(solution())
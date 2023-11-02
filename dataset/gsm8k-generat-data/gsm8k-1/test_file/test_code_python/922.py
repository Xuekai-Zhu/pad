def solution():
    """Colby loves going to the movies and every month his parents give him $150 to spend at the movies. Tickets for Fridays and Saturdays cost $10. Tickets for any other day cost $7. Popcorn costs $8 and boxes of candy cost $2. It is the last day of the month and it's a Friday. He wants to make sure he gets a popcorn and box of candy that night. How many movies can he see if he already saw 5 movies on a Friday or Saturday, 8 movies on other days, had 2 tubs of popcorn, and four boxes of candy that month?"""
    budget = 150
    friday_saturday_price = 10
    other_days_price = 7
    popcorn_price = 8
    candy_price = 2
    movies_watched = 5 + 8
    popcorns_eaten = 2
    candies_eaten = 4
    total_spent = (movies_watched * friday_saturday_price) + (8 * other_days_price) + \
                  (popcorns_eaten * popcorn_price) + (candies_eaten * candy_price)
    remaining_budget = budget - total_spent
    movies_possible = remaining_budget // (friday_saturday_price + popcorn_price + candy_price)
    result = movies_possible
    
    return result

print(solution())
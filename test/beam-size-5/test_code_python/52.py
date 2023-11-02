def solution():
    ticket_price = 7  # Peter always gets a ticket for $7
    popcorn_price = 7  # Peter always gets a popcorn for $7
    total_money = 42  # Peter has 42 dollars for the week

    # Calculate how many times Peter can go to the movies Peter can go to the movies
    times_to_go_to_movies = (total_money - ticket_price - popcorn_price) / ticket_price
    result = times_to_go_to_movies
    return result

print(solution())
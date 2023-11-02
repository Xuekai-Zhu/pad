def solution():
    """In a movie theater, the admission costs $8 but the price is $3 less if you watch the movie before 6 P.M. Kath takes her 2 siblings and 3 of her friends to a movie which starts at 4 P.M. How much will Kath pay for all of their admission?"""
    regular_price = 8
    early_bird_price = regular_price - 3
    num_tickets = 2 + 3  # Kath's 2 siblings + 3 friends
    total_regular_price = num_tickets * regular_price
    num_early_bird_tickets = num_tickets
    total_early_bird_price = num_early_bird_tickets * early_bird_price
    total_price = total_regular_price + total_early_bird_price
    result = total_price
    return result

print(solution())
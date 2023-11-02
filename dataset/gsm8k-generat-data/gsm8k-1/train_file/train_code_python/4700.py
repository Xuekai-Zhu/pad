def solution():
    """In a movie theater, the admission costs $8 but the price is $3 less if you watch the movie before 6 P.M. Kath takes her 2 siblings and 3 of her friends to a movie which starts at 4 P.M. How much will Kath pay for all of their admission?"""
    regular_price = 8
    discount_price = regular_price - 3
    num_people = 5 # Kath's 2 siblings and 3 friends
    total_cost = num_people * discount_price
    result = total_cost
    return result

print(solution())
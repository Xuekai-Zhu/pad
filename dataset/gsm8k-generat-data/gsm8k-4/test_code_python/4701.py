def solution():
    """In a movie theater, the admission costs $8 but the price is $3 less if you watch the movie before 6 P.M. Kath takes her 2 siblings and 3 of her friends to a movie which starts at 4 P.M. How much will Kath pay for all of their admission?"""
    # Define the regular and early bird admission prices
    regular_price = 8
    early_bird_price = 5

    # Calculate the total number of people watching the movie
    total_people = 2 + 2 + 3

    # Calculate the total cost of admission
    admission_cost = (2 * early_bird_price) + (3 * early_bird_price) + (2 * regular_price)

    # return the result
    result = admission_cost
    return result

print(solution())
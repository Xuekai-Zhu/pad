def solution():
    """In a movie theater, the admission costs $8 but the price is $3 less if you watch the movie before 6 P.M. Kath takes her 2 siblings and 3 of her friends to a movie which starts at 4 P.M. How much will Kath pay for all of their admission?"""
    # Define the regular and early bird admission prices
    REGULAR_PRICE = 8
    EARLY_BIRD_PRICE = 5

    # Define the number of people watching the movie
    NUM_PEOPLE = 5 + 2

    # Calculate the total cost of admission
    total_cost = NUM_PEOPLE * EARLY_BIRD_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())
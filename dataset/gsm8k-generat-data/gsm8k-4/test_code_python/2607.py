def solution():
    """John's dog has a litter of 8 puppies. He gives away half of them. He keeps one of the remaining puppies. He then takes the remaining puppies and sells them each for $600. He had to give the owner of the stud $300. How much money does he profit?"""
    # Define the initial number of puppies and the price per puppy
    INITIAL_PUPPIES = 8
    PRICE_PER_PUPPY = 600

    # Calculate the number of given away puppies
    given_away_puppies = INITIAL_PUPPIES / 2

    # Calculate the number of remaining puppies
    remaining_puppies = INITIAL_PUPPIES - given_away_puppies - 1

    # Calculate the revenue from selling the remaining puppies
    revenue = remaining_puppies * PRICE_PER_PUPPY

    # Calculate the total profit
    profit = revenue - 300

    # return the result
    result = profit
    return result

print(solution())
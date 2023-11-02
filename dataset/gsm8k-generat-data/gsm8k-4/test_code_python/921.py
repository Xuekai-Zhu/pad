def solution():
    """There were 90 people at the summer picnic. There were 50 soda cans, 50 plastic bottles of sparkling water, and 50 glass bottles of juice. One-half of the guests drank soda, one-third of the guests drank sparkling water, and four-fifths of the juices were consumed. How many recyclable cans and bottles were collected?"""
    # Define the number of people and the number of each type of drink
    num_people = 90
    num_soda_cans = 50
    num_sparkling_bottles = 50
    num_juice_bottles = 50

    # Calculate the number of people who drank each type of drink
    num_soda_drinkers = num_people / 2
    num_sparkling_drinkers = num_people / 3
    num_juice_drinkers = num_people * (4 / 5)

    # Calculate the total number of cans and bottles collected
    num_recyclables = (num_soda_drinkers * 1) + (num_sparkling_drinkers * 1) + (num_juice_drinkers * 1)

    # Return the result
    result = num_recyclables
    return result

print(solution())
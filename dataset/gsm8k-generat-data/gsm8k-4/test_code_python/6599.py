def solution():
    """Johnson has a sack of potatoes. He gives Gina 69 potatoes, gives Tom twice as much potatoes as he gave Gina and gives one-third of the amount of potatoes he gave Tom to Anne. How many potatoes does he have left if the sack contains 300 potatoes?"""
    # Define the initial number of potatoes
    potatoes = 300

    # Calculate the number of potatoes given to Gina and subtract it from the initial number of potatoes
    potatoes_given_gina = 69
    potatoes -= potatoes_given_gina

    # Calculate the number of potatoes given to Tom and subtract it from the current number of potatoes
    potatoes_given_tom = potatoes_given_gina * 2
    potatoes -= potatoes_given_tom

    # Calculate the number of potatoes given to Anne and subtract it from the current number of potatoes
    potatoes_given_anne = potatoes_given_tom / 3
    potatoes -= potatoes_given_anne

    # return the result
    result = potatoes
    return result

print(solution())
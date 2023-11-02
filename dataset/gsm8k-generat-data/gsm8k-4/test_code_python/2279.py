def solution():
    """Austin has 10 pairs of dress shoes he needs to polish over the weekend. If he has polished 45% of individual shoes, how many more shoes does he need to polish?"""
    # Define the number of pairs of shoes and the percentage already polished
    num_shoe_pairs = 10
    percent_polished = 0.45

    # Calculate the total number of shoes
    num_shoes = num_shoe_pairs * 2

    # Calculate the number of shoes already polished
    num_polished = round(num_shoes * percent_polished)

    # Calculate the number of shoes still to be polished
    num_to_polish = num_shoes - num_polished

    # return the result
    result = num_to_polish
    return result

print(solution())
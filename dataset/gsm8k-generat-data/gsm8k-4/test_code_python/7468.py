def solution():
    """Very early this morning, Elise left home in a cab headed for the hospital. Fortunately, the roads were clear, and the cab company only charged her a base price of $3, and $4 for every mile she traveled. If Elise paid a total of $23, how far is the hospital from her house?"""
    # Define the base price and cost per mile
    BASE_PRICE = 3
    COST_PER_MILE = 4

    # Calculate the distance traveled
    distance = (23 - BASE_PRICE) / COST_PER_MILE

    # return the result
    result = distance
    return result

print(solution())
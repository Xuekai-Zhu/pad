def solution():
    """Gary is buying chlorine for his rectangular pool, which is 10 feet long, 8 feet wide, and 6 feet deep. Gary needs to buy one quart of chlorine for every 120 cubic feet of water in his pool. If chlorine costs $3 a quart, how much does Gary spend on chlorine?"""
    # Define the dimensions of the pool
    length = 10
    width = 8
    depth = 6

    # Calculate the volume of the pool
    volume = length * width * depth

    # Calculate the amount of chlorine needed
    chlorine_needed = volume / 120

    # Calculate the cost of the chlorine
    chlorine_cost = chlorine_needed * 3

    # return the result
    result = chlorine_cost
    return result

print(solution())
def solution():
    """Dana Point beach has four times the number of sharks as Newport Beach. If Newport Beach has 22 sharks, how many sharks are there in total on the two beaches?"""
    # Define the number of sharks in Newport Beach
    newport_sharks = 22

    # Calculate the number of sharks in Dana Point beach
    dana_sharks = newport_sharks * 4

    # Calculate the total number of sharks
    total_sharks = newport_sharks + dana_sharks

    # return the result
    result = total_sharks
    return result

print(solution())
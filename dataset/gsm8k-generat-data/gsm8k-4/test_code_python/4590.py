def solution():
    """Last week, a farmer shipped 10 boxes of pomelos which had 240 pomelos in all. This week, the farmer shipped 20 boxes. How many dozens of pomelos did the farmer ship in all?"""
    # Define the total number of pomelos shipped in the two weeks
    total_pomelos = 240 + (20 * 12)

    # Calculate the number of dozens of pomelos
    dozens_pomelos = total_pomelos / 12

    # return the result
    result = dozens_pomelos
    return result

print(solution())
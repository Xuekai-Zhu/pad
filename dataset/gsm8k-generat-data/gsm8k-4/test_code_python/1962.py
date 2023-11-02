def solution():
    """Philip is a painter. He makes 2 paintings per day. If he already has 20 paintings, how many paintings in total will he have after 30 days?"""
    # Define the initial number of paintings and the number of paintings painted each day
    initial_paintings = 20
    paintings_per_day = 2

    # Calculate the total number of paintings after 30 days
    total_paintings = initial_paintings + (paintings_per_day * 30)

    # return the result
    result = total_paintings
    return result

print(solution())
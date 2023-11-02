def solution():
    """In preparation for the church fundraiser, Julia bakes one less than 5 cakes per day for 6 days. Unfortunately, every other day, Julia's brother, Clifford, sneaks into Julia's house and eats one of Julia's cakes. At the end of 6 days, how many cakes does Julia have remaining?"""
    # Define the number of cakes Julia bakes per day
    cakes_per_day = 4

    # Calculate the total number of cakes Julia bakes
    total_cakes = cakes_per_day * 6

    # Subtract the number of cakes Clifford eats (one every other day)
    total_cakes -= 3

    # Return the number of cakes remaining
    result = total_cakes
    return result

print(solution())
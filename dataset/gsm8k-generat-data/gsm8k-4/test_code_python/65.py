def solution():
    """Lee mows one lawn and charges $33. Last week he mowed 16 lawns and three customers each gave him a $10 tip. How many dollars did Lee earn mowing lawns last week?"""
    # Define the cost to mow one lawn and the number of lawns mowed last week
    LAWN_COST = 33
    LAWNS_MOWED = 16

    # Calculate the total revenue from mowing lawns
    lawn_revenue = LAWN_COST * LAWNS_MOWED

    # Calculate the total tips received
    total_tips = 3 * 10

    # Calculate the total earnings
    earnings = lawn_revenue + total_tips

    result = earnings
    return result

print(solution())
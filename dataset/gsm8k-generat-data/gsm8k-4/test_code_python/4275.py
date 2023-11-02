def solution():
    """Scott, Mary, and Ken committed to raising $4,000 for their local children’s cancer hospital. Right now, Mary’s collection is five times what Ken has, but three times Scott’s funds. If Ken has $600, by how much have the three exceeded their goal?"""
    # Define the target fundraising goal
    fundraising_goal = 4000

    # Define Ken's fundraising amount
    ken_fundraising = 600

    # Calculate Mary's fundraising amount
    mary_fundraising = ken_fundraising * 5

    # Calculate Scott's fundraising amount
    scott_fundraising = mary_fundraising / 3

    # Calculate the total fundraising amount
    total_fundraising = ken_fundraising + mary_fundraising + scott_fundraising

    # Calculate the amount by which the goal has been exceeded
    amount_exceeded = total_fundraising - fundraising_goal

    # return the result
    result = amount_exceeded
    return result

print(solution())
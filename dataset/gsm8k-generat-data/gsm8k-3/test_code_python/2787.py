def solution():
    """Remi wants to drink more water. He has a refillable water bottle that holds 20 ounces of water. That week Remi refills the bottle 3 times a day and drinks the whole bottle each time except for twice when he accidentally spills 5 ounces the first time and 8 ounces the second time. In 7 days how many ounces of water does Remi drink?"""
    # Calculate how many ounces of water Remi drinks each day
    ounces_per_day = 20 * 3 - 5 - 8

    # Calculate how many ounces of water Remi drinks in a week
    ounces_in_week = ounces_per_day * 7

    # Display how many ounces of water Remi drinks in a week
    result = ounces_in_week
    return result

print(solution())
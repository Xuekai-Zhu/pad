def solution():
    """Jane's mother agreed to pay her $.50 for every flower bulb that Jane planted.  Jane planted 20 tulip bulbs and half that amount of iris bulbs.  She also planted 30 daffodil bulbs and three times that amount of crocus bulbs.  How much money did Jane earn?"""
    # Define the rate that Jane's mother pays per flower bulb
    RATE_PER_BULB = 0.5

    # Calculate the number of iris bulbs that Jane planted
    iris_bulbs = 20 / 2

    # Calculate the number of crocus bulbs that Jane planted
    crocus_bulbs = 30 * 3

    # Calculate the total number of bulbs that Jane planted
    total_bulbs = 20 + iris_bulbs + 30 + crocus_bulbs

    # Calculate Jane's earnings
    earnings = total_bulbs * RATE_PER_BULB

    # Display Jane's earnings
    result = earnings
    return result

print(solution())
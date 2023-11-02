def solution():
    """The Chrysler Building has 11 more floors than the Leeward Center. Together they have a total of 35 floors. How many floors does the Chrysler Building have?"""
    # Let's assume the number of floors in the Leeward Center as x
    # Then, the number of floors in the Chrysler Building will be (x+11)

    # The total number of floors is 35, so we can write an equation:
    # x + (x+11) = 35
    # Solving for x gives x = 12

    # Therefore, the number of floors in the Chrysler Building is:
    chrysler_floors = 12 + 11

    # return the result
    result = chrysler_floors
    return result

print(solution())
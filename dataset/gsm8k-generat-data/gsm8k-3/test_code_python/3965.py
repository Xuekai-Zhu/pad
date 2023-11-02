def solution():
    """Dallas and Austin went to the pick-your-own orchard.
    Dallas picked 14 bags of apples and 9 bags of pears.
    Austin picked 6 bags of apples more than Dallas, and 5 fewer bags of pears than Dallas.
    How many bags of fruit did Austin pick, in total?"""
    # Define the number of bags Dallas picked
    dallas_apples = 14
    dallas_pears = 9

    # Define the number of bags Austin picked
    austin_apples = dallas_apples + 6
    austin_pears = dallas_pears - 5

    # Calculate the total number of bags Austin picked
    total_bags = austin_apples + austin_pears

    # Display the total number of bags Austin picked
    result = total_bags
    return result

print(solution())
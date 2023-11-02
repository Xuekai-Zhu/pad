def solution():
    """Dallas and Austin went to the pick-your-own orchard. Dallas picked 14 bags of apples and 9 bags of pears. Austin picked 6 bags of apples more than Dallas, and 5 fewer bags of pears than Dallas. How many bags of fruit did Austin pick, in total?"""
    # Define the number of bags picked by Dallas
    dallas_apples = 14
    dallas_pears = 9

    # Calculate the number of bags picked by Austin
    austin_apples = dallas_apples + 6
    austin_pears = dallas_pears - 5

    # Calculate the total number of bags picked by Austin
    total_bags_austin = austin_apples + austin_pears

    result = total_bags_austin
    return result

print(solution())
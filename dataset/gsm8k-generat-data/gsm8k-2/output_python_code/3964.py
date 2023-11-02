def solution():
    """Dallas and Austin went to the pick-your-own orchard. Dallas picked 14 bags of apples and 9 bags of pears. Austin picked 6 bags of apples more than Dallas, and 5 fewer bags of pears than Dallas. How many bags of fruit did Austin pick, in total?"""
    dallas_apples = 14
    dallas_pears = 9
    austin_apples = dallas_apples + 6
    austin_pears = dallas_pears - 5
    total_bags = dallas_apples + dallas_pears + austin_apples + austin_pears
    result = total_bags
    return result

print(solution())
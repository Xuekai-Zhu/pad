def solution():
    """Jack has 65 pounds of sugar today. Tomorrow he will use 18 pounds of sugar and the following day he will buy 50 more pounds of sugar. How many pounds will he have in the end?"""
    starting_amount = 65
    used_amount = 18
    bought_amount = 50
    end_amount = starting_amount - used_amount + bought_amount
    result = end_amount
    return result

print(solution())
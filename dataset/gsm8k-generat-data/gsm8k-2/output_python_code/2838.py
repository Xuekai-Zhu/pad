def solution():
    """Jacob is making s'mores. Each s'more takes two graham crackers and one marshmallow. If Jacob has 48 graham crackers and 6 marshmallows, how many more marshmallows does he need to buy?"""
    graham_crackers = 48
    marshmallows = 6
    smores = min(graham_crackers // 2, marshmallows)
    remaining_marshmallows = marshmallows - smores
    if remaining_marshmallows < 0:
        remaining_marshmallows = 0
    result = remaining_marshmallows
    return result

print(solution())
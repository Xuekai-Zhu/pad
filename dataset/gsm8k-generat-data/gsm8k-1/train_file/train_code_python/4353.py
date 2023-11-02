def solution():
    """Joe goes camping with his dad on a Friday. Joe's dad has 21 marshmallows, and Joe has four times as much marshmallows as his dad. If Joe’s dad roasts a third of his marshmallows, and Joe roasts half of his marshmallows, how many marshmallows did they roast in total?"""
    dad_marshmallows = 21
    joe_marshmallows = 4 * dad_marshmallows
    dad_roast = dad_marshmallows / 3
    joe_roast = joe_marshmallows / 2
    total_roast = dad_roast + joe_roast
    result = total_roast
    return result

print(solution())
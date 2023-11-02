def solution():
    """Joe goes camping with his dad on a Friday. Joe's dad has 21 marshmallows, and Joe has four times as much marshmallows as his dad. If Joe’s dad roasts a third of his marshmallows, and Joe roasts half of his marshmallows, how many marshmallows did they roast in total?"""
    dad_marshmallows = 21
    joe_marshmallows = dad_marshmallows * 4
    dad_roasted = dad_marshmallows // 3
    joe_roasted = joe_marshmallows // 2
    total_roasted = dad_roasted + joe_roasted
    result = total_roasted
    return result

print(solution())
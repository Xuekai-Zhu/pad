def solution():
    """Joe goes camping with his dad on a Friday. Joe's dad has 21 marshmallows, and Joe has four times as much marshmallows as his dad. If Joe’s dad roasts a third of his marshmallows, and Joe roasts half of his marshmallows, how many marshmallows did they roast in total?"""
    # Define the number of marshmallows Joe's dad has
    dads_marshmallows = 21

    # Define the number of marshmallows Joe has
    joes_marshmallows = dads_marshmallows * 4

    # Calculate the number of marshmallows Joe's dad roasts
    dads_roasted_marshmallows = dads_marshmallows / 3

    # Calculate the number of marshmallows Joe roasts
    joes_roasted_marshmallows = joes_marshmallows / 2

    # Calculate the total number of marshmallows roasted
    total_roasted_marshmallows = dads_roasted_marshmallows + joes_roasted_marshmallows

    result = total_roasted_marshmallows
    return result

print(solution())
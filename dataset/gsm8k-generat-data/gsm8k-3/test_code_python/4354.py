def solution():
    """Joe goes camping with his dad on a Friday. Joe's dad has 21 marshmallows, and Joe has four times as much marshmallows as his dad. If Joe’s dad roasts a third of his marshmallows, and Joe roasts half of his marshmallows, how many marshmallows did they roast in total?"""
    # Define the number of marshmallows Joe's dad has
    dad_marshmallows = 21

    # Calculate the number of marshmallows Joe has
    joe_marshmallows = 4 * dad_marshmallows

    # Calculate the number of marshmallows Joe's dad roasts
    dad_roasted = dad_marshmallows / 3

    # Calculate the number of marshmallows Joe roasts
    joe_roasted = joe_marshmallows / 2

    # Calculate the total number of marshmallows roasted
    total_roasted = dad_roasted + joe_roasted

    # Display the total number of marshmallows roasted
    result = total_roasted
    return result

print(solution())
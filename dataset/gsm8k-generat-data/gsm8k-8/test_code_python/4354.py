def solution():
    # Define the number of marshmallows Joe's dad has
    dad_marshmallows = 21

    # Define the number of marshmallows Joe has (four times as much as his dad)
    joe_marshmallows = 4 * dad_marshmallows

    # Calculate the number of marshmallows Joe's dad roasts (one-third of his marshmallows)
    dad_roasted_marshmallows = dad_marshmallows / 3

    # Calculate the number of marshmallows Joe roasts (half of his marshmallows)
    joe_roasted_marshmallows = joe_marshmallows / 2

    # Calculate the total number of marshmallows roasted
    total_roasted_marshmallows = dad_roasted_marshmallows + joe_roasted_marshmallows

    result = total_roasted_marshmallows
    return result

print(solution())
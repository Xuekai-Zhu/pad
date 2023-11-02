def solution():
    dad_marshmallows = 21
    joe_marshmallows = 4 * dad_marshmallows

    # Calculate the number of marshmallows Joe's dad roasted
    dad_roasted = dad_marshmallows / 3

    # Calculate the number of marshmallows Joe roasted
    joe_roasted = joe_marshmallows / 2

    # Calculate the total number of marshmallows roasted
    total_roasted = dad_roasted + joe_roasted
    result = total_roasted
    return result

print(solution())
def solution():
    dad_marshmallows = 21
    joe_marshmallows = 4 * dad_marshmallows

    # Calculate the number of marshmallows roasted by Joe's dad and Joe
    dad_roasted = dad_marshmallows / 3
    joe_roasted = joe_marshmallows / 2

    # Calculate the total number of marshmallows roasted
    total_roasted = dad_roasted + joe_roasted
    result = total_roasted
    return result

print(solution())
def solution():
    dad_marshmallows = 21
    joe_marshmallows = 4 * dad_marshmallows
    dad_roasts = dad_marshmallows / 3  # Dad roasts a third of his marshmallows
    joe_roasts = joe_marshmallows / 2  # Joe roasts half of his marshmallows
    total_roasts = dad_roasts + joe_roasts  # Total number of marshmallows roasted

    result = total_roasts
    return result

print(solution())
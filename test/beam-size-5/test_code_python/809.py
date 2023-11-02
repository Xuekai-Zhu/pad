def solution():
    
    total_marshmallows = 35
    john_marshmallows = 9
    desean_marshmallows = 9
    dropped_marshmallows = 3
    remaining_marshmallows = total_marshmallows - (john_marshmallows + desean_marshmallows - dropped_marshmallows)
    mores_per_kid = remaining_marshmallows // remaining_marshmallows
    result = mores_per_kid
    return result

print(solution())
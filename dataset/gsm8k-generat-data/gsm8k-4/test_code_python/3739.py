def solution():
    """Haley could hold 8 marshmallows in her mouth. Michael could hold 3 times as many marshmallows as Haley. Brandon could hold half as many as Michael. How many total marshmallows did all three kids hold in their mouths?"""
    # Calculate how many marshmallows Michael and Brandon can hold
    michael_marshmallows = 8 * 3
    brandon_marshmallows = michael_marshmallows / 2

    # Calculate the total number of marshmallows held by all three kids
    total_marshmallows = 8 + michael_marshmallows + brandon_marshmallows

    # return the result
    result = total_marshmallows
    return result

print(solution())
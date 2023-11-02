def solution():
    """Haley, Michael and Brandon were trying a marshmallow challenge to see who could hold more marshmallows in their mouths. Haley could hold 8 marshmallows in her mouth. Michael could hold 3 times as many marshmallows as Haley. Brandon could hold half as many as Michael. How many total marshmallows did all three kids hold in their mouths?"""
    haley_marshmallows = 8
    michael_marshmallows = haley_marshmallows * 3
    brandon_marshmallows = michael_marshmallows / 2
    total_marshmallows = haley_marshmallows + michael_marshmallows + brandon_marshmallows
    result = total_marshmallows
    return result

print(solution())
def solution():
    """The Kennel house keeps 3 German Shepherds and 2 Bulldogs. If a German Shepherd consumes 5 kilograms of dog food and a bulldog consumes 3 kilograms of dog food per day. How many kilograms of dog food will they need in a week?"""
    german_shepherds = 3
    bulldogs = 2
    food_per_day = (german_shepherds * 5) + (bulldogs * 3)
    food_per_week = food_per_day * 7
    result = food_per_week
    return result

print(solution())
def solution():
    """At camp Wonka, there are 96 campers. Two-thirds of the campers are boys, and the remaining one-third are girls. 50% of the boys want to toast marshmallows and 75% of the girls want to toast marshmallows. If each camper gets one marshmallow to toast, how many marshmallows do they need?"""
    total_campers = 96
    boys = total_campers * 2 / 3
    girls = total_campers * 1 / 3
    boys_toast = boys * 0.5
    girls_toast = girls * 0.75
    total_toast = boys_toast + girls_toast
    result = total_toast
    return result

print(solution())
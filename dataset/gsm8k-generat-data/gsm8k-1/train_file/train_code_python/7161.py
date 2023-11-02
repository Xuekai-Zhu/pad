def solution():
    """The chicken crossed the road to get to the other side twice for the thrill of it. The first time, it had to dodge 23 speeding cars. The second time, a person tried to catch it and accidentally pulled out twice as many feathers as the number of cars the chicken had dodged. The chicken had 5263 feathers before its thrill-seeking road crossings. How many feathers did it have afterward?"""
    cars_dodged = 23
    feathers_before = 5263
    feathers_pulled = cars_dodged * 2
    feathers_after = feathers_before - feathers_pulled
    result = feathers_after
    return result

print(solution())
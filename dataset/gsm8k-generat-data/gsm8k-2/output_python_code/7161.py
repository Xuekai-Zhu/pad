def solution():
    """The chicken crossed the road to get to the other side twice for the thrill of it. The first time, it had to dodge 23 speeding cars. The second time, a person tried to catch it and accidentally pulled out twice as many feathers as the number of cars the chicken had dodged. The chicken had 5263 feathers before its thrill-seeking road crossings. How many feathers did it have afterward?"""
    initial_feathers = 5263
    cars_dodged = 23
    feathers_pulled = 2 * cars_dodged
    remaining_feathers = initial_feathers - feathers_pulled
    total_feathers = remaining_feathers
    return total_feathers

print(solution())
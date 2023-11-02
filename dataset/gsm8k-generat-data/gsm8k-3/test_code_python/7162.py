def solution():
    """The chicken crossed the road to get to the other side twice for the thrill of it. The first time, it had to dodge 23 speeding cars. The second time, a person tried to catch it and accidentally pulled out twice as many feathers as the number of cars the chicken had dodged. The chicken had 5263 feathers before its thrill-seeking road crossings. How many feathers did it have afterward?"""
    # Calculate the number of feathers pulled out during the second crossing
    feathers_pulled = 2 * 23

    # Calculate the number of feathers the chicken has left
    feathers_left = 5263 - feathers_pulled

    # Display the number of feathers the chicken has left
    result = feathers_left
    return result

print(solution())
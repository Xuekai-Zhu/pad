def solution():
    """The chicken crossed the road to get to the other side twice for the thrill of it. The first time, it had to dodge 23 speeding cars. The second time, a person tried to catch it and accidentally pulled out twice as many feathers as the number of cars the chicken had dodged. The chicken had 5263 feathers before its thrill-seeking road crossings. How many feathers did it have afterward?"""
    # Define the initial number of feathers
    initial_feathers = 5263

    # Calculate the number of feathers pulled out in the second crossing
    feathers_pulled = 23 * 2

    # Calculate the remaining number of feathers
    remaining_feathers = initial_feathers - feathers_pulled

    # Calculate the number of feathers after the second crossing
    final_feathers = remaining_feathers - feathers_pulled * 2

    # Return the result
    result = final_feathers
    return result

print(solution())
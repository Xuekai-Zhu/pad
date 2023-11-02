def solution():
    """Joanna and Jacques had 40 and 60 gumballs, respectively, in their dishes. They then purchased 4 times the number of gumballs they had initially and added these to their dishes. If they decided to put together their gumballs and shared them equally, how many gumballs did each get?"""
    # Define the initial number of gumballs
    joanna_gumballs = 40
    jacques_gumballs = 60

    # Calculate the number of gumballs purchased
    purchased_gumballs = 4 * (joanna_gumballs + jacques_gumballs)

    # Add the purchased gumballs to their dishes
    joanna_gumballs += purchased_gumballs
    jacques_gumballs += purchased_gumballs

    # Calculate the total number of gumballs
    total_gumballs = joanna_gumballs + jacques_gumballs

    # Calculate the number of gumballs each gets when shared equally
    each_gets = total_gumballs // 2

    # Return the result
    result = each_gets
    return result

print(solution())
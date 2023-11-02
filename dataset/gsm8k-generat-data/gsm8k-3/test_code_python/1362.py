def solution():
    """Joanna and Jacques had 40 and 60 gumballs, respectively, in their dishes. They then purchased 4 times the number of gumballs they had initially and added these to their dishes. If they decided to put together their gumballs and shared them equally, how many gumballs did each get?"""
    # Define the initial number of gumballs in Joanna and Jacques' dishes
    JOANNA_GUMBALLS = 40
    JACQUES_GUMBALLS = 60

    # Define the multiplier for the additional gumballs purchased
    ADDITIONAL_MULTIPLIER = 4

    # Calculate the total number of gumballs after the additional purchase
    total_gumballs = (JOANNA_GUMBALLS + JACQUES_GUMBALLS) * ADDITIONAL_MULTIPLIER

    # Calculate the number of gumballs each person gets if shared equally
    each_person = total_gumballs / 2

    # Display the number of gumballs each person gets
    result = each_person
    return result

print(solution())
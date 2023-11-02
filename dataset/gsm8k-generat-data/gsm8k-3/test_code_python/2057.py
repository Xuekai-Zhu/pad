def solution():
    """Jack, who weighs 60 pounds, wants to play on the see-saw with his cousin Anna, who weighs 40 pounds. How many 4-pound rocks does Jack need to hold to make their weights equal?"""
    # Define the weights of Jack and Anna
    jack_weight = 60
    anna_weight = 40

    # Calculate the weight difference between Jack and Anna
    weight_difference = jack_weight - anna_weight

    # Calculate the number of 4-pound rocks Jack needs to hold to make the weights equal
    rocks_needed = weight_difference / 4

    # Display the number of rocks needed
    result = rocks_needed
    return result

print(solution())
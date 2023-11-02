def solution():
    """Michael’s largest watermelon weighs 8 pounds.  His neighbor, Clay, grew a watermelon three times that size.  And their mutual friend, John, grew a watermelon that was half the size of Clay’s.  How big was John’s watermelon?"""
    # Define the weight of Michael's watermelon
    michael_weight = 8

    # Define the weight of Clay's watermelon
    clay_weight = michael_weight * 3

    # Define the weight of John's watermelon
    john_weight = clay_weight / 2

    # Display the weight of John's watermelon
    result = john_weight
    return result

print(solution())
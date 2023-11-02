def solution():
    """Rachel weighs 75 pounds, 6 pounds less than Jimmy and 15 pounds more than Adam. What is the average weight of the three people, in pounds?"""
    # Define Rachel's weight
    rachel_weight = 75

    # Calculate Jimmy's weight
    jimmy_weight = rachel_weight + 6

    # Calculate Adam's weight
    adam_weight = rachel_weight - 15

    # Calculate the total weight of the three people
    total_weight = rachel_weight + jimmy_weight + adam_weight

    # Calculate the average weight
    average_weight = total_weight / 3

    # Display the average weight
    result = average_weight
    return result

print(solution())
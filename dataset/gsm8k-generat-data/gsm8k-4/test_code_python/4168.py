def solution():
    """Rachel weighs 75 pounds, 6 pounds less than Jimmy and 15 pounds more than Adam. What is the average weight of the three people, in pounds?"""
    # Define the weight of Rachel, Jimmy, and Adam
    rachel_weight = 75
    jimmy_weight = rachel_weight + 6
    adam_weight = rachel_weight - 15

    # Calculate the average weight of the three people
    average_weight = (rachel_weight + jimmy_weight + adam_weight) / 3

    result = average_weight
    return result

print(solution())
def solution():
    """Alice is making a big stack of dishes to see how tall she can make it before it topples over and falls. She starts off by placing 27 plates on top of each other. The tower holds fine so she adds 37 more plates. She is in the process of placing more and more plates when it finally topples over and crashes down, all 83 plates. How many more was Alice able to add before the tower fell and crashed?"""
    # Define the initial number of plates and the number added before it toppled
    initial_plates = 27
    added_before_toppled = 37

    # Calculate the number of plates standing before it toppled
    standing_plates = 83 - added_before_toppled

    # Calculate the number of plates Alice was able to add before it toppled
    added_before_toppled = standing_plates - initial_plates

    # Display the number of plates Alice was able to add before it toppled
    result = added_before_toppled
    return result

print(solution())
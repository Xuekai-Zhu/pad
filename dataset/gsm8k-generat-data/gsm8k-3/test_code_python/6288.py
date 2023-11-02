def solution():
    """Alice is making a big stack of dishes to see how tall she can make it before it topples over and falls. She starts off by placing 27 plates on top of each other. The tower holds fine so she adds 37 more plates. She is in the process of placing more and more plates when it finally topples over and crashes down, all 83 plates. How many more was Alice able to add before the tower fell and crashed?"""
    # Define the initial number of plates
    initial_plates = 27

    # Add the next batch of plates
    total_plates = initial_plates + 37

    # Calculate how many more plates Alice was able to add before the tower fell
    remaining_plates = 83 - total_plates

    # Display how many more plates Alice added before the tower fell
    result = remaining_plates
    return result

print(solution())
def solution():
    """Alice is making a big stack of dishes to see how tall she can make it before it topples over and falls. She starts off by placing 27 plates on top of each other. The tower holds fine so she adds 37 more plates. She is in the process of placing more and more plates when it finally topples over and crashes down, all 83 plates. How many more was Alice able to add before the tower fell and crashed?"""
    initial_plates = 27
    added_plates = 37
    total_plates = 83
    remaining_plates = total_plates - initial_plates - added_plates
    result = remaining_plates
    return result

print(solution())
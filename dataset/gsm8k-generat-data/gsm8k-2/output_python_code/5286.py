def solution():
    """Dennis lives two floors above Charlie. Charlie lives on a floor whose number is 1/4 Frank's floor number. Frank lives on the 16th floor. What floor does Dennis live on?"""
    frank_floor = 16
    charlie_floor = frank_floor / 4
    dennis_floor = charlie_floor + 2
    result = dennis_floor
    return result

print(solution())
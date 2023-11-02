def solution():
    # Calculate the number of turns the wheel makes in 30 seconds
    turns_per_30_seconds = 6  

    # Calculate the number of turns the wheel makes in two hours (7200 seconds)
    turns_in_two_hours = turns_per_30_seconds * (7200/30)  
    result = turns_in_two_hours
    return result

print(solution())
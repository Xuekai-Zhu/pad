def solution():
    # Calculate the total number of steps forward that Frank is from his starting point
    total_steps_forward = 10 + (2*2*2)  # Frank takes 10 steps forward and then doubles his previous 2 steps forward twice
    total_steps_back = 5 + 2  # Frank takes 5 steps back and then 2 steps back
    result = total_steps_forward - total_steps_back
    return result

print(solution())
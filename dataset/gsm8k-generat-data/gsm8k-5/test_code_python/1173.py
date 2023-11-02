def solution():
    total_time = 10  # Audrey was asleep for 10 hours
    dream_time = (2/5) * total_time  # Audrey dreamed for 2/5 of the time
    not_dream_time = total_time - dream_time  # Calculate the time Audrey was not dreaming
    result = not_dream_time
    return result

print(solution())
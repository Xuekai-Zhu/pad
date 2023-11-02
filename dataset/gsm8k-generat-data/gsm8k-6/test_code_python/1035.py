def solution():
    # Find the total number of girls at the event
    num_girls = 600 - 400  # difference between boys and girls is 400, and there are 600 boys
    total_people = num_girls + 600  # total number of people at the event

    # Calculate 60% of the total number of boys and girls
    percent = 0.6  # 60%
    result = int(percent * total_people)
    return result

print(solution())
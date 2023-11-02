def solution():
    num_paintings = 12
    time_taken = 6
    additional_paintings = 20

    # Calculate the time taken to paint one painting
    time_per_painting = time_taken / num_paintings

    # Calculate the total time taken to paint all paintings
    total_time = time_taken + (additional_paintings * time_per_painting)
    result = total_time
    return result

print(solution())
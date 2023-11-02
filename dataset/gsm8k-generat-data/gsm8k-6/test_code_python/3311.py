def solution():
    # Calculate the amount Porter made on his most recent painting
    current_painting = 44000  # amount received for most recent painting
    previous_painting = (current_painting + 1000) / 5  # amount received for previous painting
    result = previous_painting
    return result

print(solution())
def solution():
    # Calculate the current depth of the treasure
    current_depth = 8 - (1/2)*8 + 2  # half of the sand was washed away, and 2 feet of new sand was added
    digging_speed = 1  # Pirate Rick can dig up 1 foot of sand per hour
    time_to_dig = current_depth / digging_speed
    result = time_to_dig
    return result

print(solution())
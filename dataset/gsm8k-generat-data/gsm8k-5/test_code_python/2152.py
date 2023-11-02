def solution():
    total_jellybeans = 70  # Aunt Angela has 70 jellybeans in the jar
    num_nephews = 3
    num_nieces = 2

    # Calculate the total number of jellybeans each child will receive
    total_per_child = total_jellybeans / (num_nephews + num_nieces)

    result = total_per_child
    return result

print(solution())
def solution():
    # Calculate the maximum amount of rum Don can consume for a healthy diet
    max_rum = 3 * 10  # Don can consume a maximum of 3 times that amount of rum for a healthy diet

    # Calculate the amount of rum Don has already consumed
    consumed_rum = 12  # Don had 12oz of rum earlier that day

    # Calculate the remaining amount of rum Don can consume
    remaining_rum = max_rum - consumed_rum

    # Add the 10oz of rum on the pancakes to the remaining amount of rum Don can consume
    total_rum = remaining_rum + 10

    result = total_rum
    return result

print(solution())
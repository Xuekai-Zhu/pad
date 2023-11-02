def solution():
    # Calculate the initial total number of fish caught
    total_fish = 16 + 10  # Will caught 16 catfish and 10 eels
    trout_caught = 3 * 16  # Henry catches 3 trout for every catfish Will catches
    total_fish += trout_caught  # Add the trout caught by Henry to the total number of fish caught
    remaining_trout = trout_caught / 2  # Henry decides to return half his catch
    total_fish -= remaining_trout  # Subtract the returned trout from the total number of fish caught
    result = total_fish
    return result

print(solution())
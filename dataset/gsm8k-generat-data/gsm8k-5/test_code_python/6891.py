def solution():
    ben_fish = 4  # Ben caught 4 fish
    judy_fish = 1  # Judy caught 1 fish
    billy_fish = 3  # Billy caught 3 fish
    jim_fish = 2  # Jim caught 2 fish
    susie_fish = 5  # Susie caught 5 fish

    total_fish = ben_fish + judy_fish + billy_fish + jim_fish + susie_fish  # Total number of fish caught
    total_fish = total_fish - 3  # Remove 3 fish that were too small

    total_filets = total_fish * 2  # Calculate total number of fish filets

    result = total_filets
    return result

print(solution())
def solution():
    # Calculate the total number of fish caught
    total_fish = 4 + 1 + 3 + 2 + 5  # Ben caught 4, Judy caught 1, Billy caught 3, Jim caught 2, Susie caught 5
    total_fish -= 3  # Subtract the 3 small fish that were thrown back
    total_filets = 2 * total_fish  # Each fish will give 2 filets
    result = total_filets
    return result

print(solution())
def solution():
    rhinestones_needed = 45  # Andrea needs 45 rhinestones to finish her art project
    bought = rhinestones_needed / 3  # Andrea bought a third of what she needed
    found = rhinestones_needed / 5  # Andrea found a fifth of what she needed

    # Calculate how many rhinestones Andrea still needs
    still_needed = rhinestones_needed - bought - found
    result = still_needed
    return result

print(solution())
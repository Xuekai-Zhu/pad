def solution():
    total_needed = 45

    # Calculate the number of rhinestones Andrea bought
    bought = total_needed // 3

    # Calculate the number of rhinestones Andrea found in her supplies
    found = total_needed // 5

    # Calculate the total number of rhinestones Andrea has
    total_have = bought + found

    # Calculate the number of rhinestones Andrea still needs
    still_need = total_needed - total_have
    result = still_need
    return result

print(solution())
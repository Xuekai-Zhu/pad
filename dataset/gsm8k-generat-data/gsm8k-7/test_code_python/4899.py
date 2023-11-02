def solution():
    friend_names = ["Jessica", "Tori", "Lily", "Patrice"]
    num_bracelets = 0

    # Calculate the total number of bracelets needed
    for name in friend_names:
        num_bracelets += len(name)

    # Calculate the total cost of all bracelets
    total_cost = num_bracelets * 2
    result = total_cost
    return result

print(solution())
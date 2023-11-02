def solution():
    # Calculate the total amount owed by everyone
    total_owed = 400 - 285  # $400 promised - $285 received

    # Calculate the amount owed by Amy and Derek
    amy_owed = 30
    derek_owed = amy_owed / 2

    # Calculate the amount owed by Sally and Carl
    sally_and_carl_owed = (total_owed - amy_owed - derek_owed) / 2

    result = sally_and_carl_owed
    return result

print(solution())
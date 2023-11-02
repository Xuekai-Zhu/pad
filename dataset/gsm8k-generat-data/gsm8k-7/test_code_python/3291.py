def solution():
    total_promised = 400
    total_received = 285
    amy_owed = 30
    derek_owed = amy_owed / 2

    # Calculate the total amount still owed by Sally, Amy, Derek, and Carl
    total_still_owed = total_promised - total_received

    # Calculate the amount still owed by Sally and Carl combined
    sally_carl_owed = total_still_owed - amy_owed - derek_owed

    # Divide the amount owed by Sally and Carl equally between the two of them
    sally_carl_each_owed = sally_carl_owed / 2

    result = sally_carl_each_owed
    return result

print(solution())
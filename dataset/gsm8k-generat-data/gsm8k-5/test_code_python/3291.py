def solution():
    # Calculate the total amount owed
    total_owed = 400 - 285  # $400 promised - $285 received = $115 still owed

    # Calculate how much Derek owes
    derek_owes = 30 / 2  # Derek owes half as much as Amy

    # Calculate the total amount owed by Sally, Carl, and Derek combined
    combined_owes = total_owed - 30 - derek_owes

    # Divide the combined amount by 2 since Sally and Carl owe the same amount
    sally_carl_owes = combined_owes / 2
    result = sally_carl_owes
    return result

print(solution())
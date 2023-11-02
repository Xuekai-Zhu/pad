def solution():
    imported_wine = 2400
    domestic_wine = imported_wine / 2
    total_bottles = imported_wine + domestic_wine

    # Calculate the number of bottles that will be drunk at the party
    drunk_bottles = total_bottles / 3

    # Calculate the number of bottles that will remain in Jose's cellar
    remaining_bottles = total_bottles - drunk_bottles
    result = remaining_bottles
    return result

print(solution())
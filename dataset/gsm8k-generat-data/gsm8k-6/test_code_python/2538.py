def solution():
    # Calculate the total number of nickels Ray has
    total_nickels = 175 / 5

    # Calculate the amount of cents Ray gives to Peter
    peter_cents = 30

    # Calculate the amount of cents Ray gives to Randi
    randi_cents = 2 * peter_cents

    # Calculate the total number of nickels Randi and Peter have after the transaction
    peter_nickels = peter_cents / 5
    randi_nickels = randi_cents / 5

    # Calculate the difference in the number of nickels between Randi and Peter
    nickels_difference = randi_nickels - peter_nickels

    result = nickels_difference
    return result

print(solution())
def solution():
    """Ray has 175 cents in nickels. Ray gives 30 cents to Peter, and he gives twice as many cents to Randi as he gave to Peter. How many more nickels does Randi have than Peter?"""
    # Define the total amount of cents Ray has in nickels
    total_cents = 175

    # Ray gives 30 cents to Peter
    peter_cents = 30

    # Ray gives twice as many cents to Randi as he gave to Peter
    randi_cents = peter_cents * 2

    # Subtract the given cents from the total cents to find how many cents Ray has left
    remaining_cents = total_cents - peter_cents - randi_cents

    # Calculate the number of nickels each person has
    peter_nickels = peter_cents // 5
    randi_nickels = randi_cents // 5
    remaining_nickels = remaining_cents // 5

    # Calculate the difference in the number of nickels between Randi and Peter
    difference = randi_nickels - peter_nickels

    # return the result
    result = difference
    return result

print(solution())
def solution():
    """Ray has 95 cents in nickels. If Ray gives 25 cents to Peter, and twice as many cents to Randi as he gave to Peter, how many nickels does Ray have left?"""
    # Define the total amount of money Ray has in cents
    total_cents = 95

    # Define the amount of money Ray gives to Peter in cents
    peter_cents = 25

    # Calculate the amount of money Ray gives to Randi in cents
    randi_cents = 2 * peter_cents

    # Calculate the total amount of money Ray gives away in cents
    given_away_cents = peter_cents + randi_cents

    # Calculate the remaining amount of money Ray has in cents
    remaining_cents = total_cents - given_away_cents

    # Calculate the number of nickels Ray has left
    num_nickels = remaining_cents // 5

    # return the result
    result = num_nickels
    return result

print(solution())
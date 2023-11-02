def solution():
    """Ray has 95 cents in nickels. If Ray gives 25 cents to Peter, and twice as many cents to Randi as he gave to Peter, how many nickels does Ray have left?"""
    # Convert 95 cents to number of nickels
    num_nickels = int(95 / 5)

    # Ray gives 25 cents to Peter
    num_nickels -= 5

    # Ray gives twice as many cents to Randi as he gave to Peter
    num_nickels -= 10

    # Calculate how many nickels Ray has left
    num_nickels_left = num_nickels

    # Display how many nickels Ray has left
    result = num_nickels_left
    return result

print(solution())
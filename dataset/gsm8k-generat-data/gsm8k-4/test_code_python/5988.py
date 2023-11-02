def solution():
    """Mark has 3 tanks for pregnant fish. Each tank has 4 pregnant fish and each fish gives birth to 20 young. How many young fish does he have at the end?"""
    # Define the number of tanks and pregnant fish per tank
    tanks = 3
    fish_per_tank = 4

    # Define the number of young fish each pregnant fish gives birth to
    young_per_fish = 20

    # Calculate the total number of pregnant fish
    total_fish = tanks * fish_per_tank

    # Calculate the total number of young fish
    total_young_fish = total_fish * young_per_fish

    # Return the result
    result = total_young_fish
    return result

print(solution())
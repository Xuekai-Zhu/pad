def solution():
    """Mark has 3 tanks for pregnant fish. Each tank has 4 pregnant fish and each fish gives birth to 20 young. How many young fish does he have at the end?"""
    # Define the number of tanks and pregnant fish per tank
    tanks = 3
    fish_per_tank = 4

    # Define the number of young each fish gives birth to
    young_per_fish = 20

    # Calculate the total number of pregnant fish
    total_pregnant_fish = tanks * fish_per_tank

    # Calculate the total number of young fish
    total_young_fish = total_pregnant_fish * young_per_fish

    # Display the total number of young fish
    result = total_young_fish
    return result

print(solution())
def solution():
    num_children = 4
    baby_spoons_per_child = 3
    num_decorative_spoons = 2
    num_large_spoons = 10
    num_teaspoons = 15

    # Calculate the total number of baby spoons
    total_baby_spoons = num_children * baby_spoons_per_child

    # Calculate the total number of spoons
    total_spoons = total_baby_spoons + num_decorative_spoons + num_large_spoons

    # Calculate the total number of teaspoons
    total_teaspoons = num_teaspoons

    # Calculate the total number of spoons Lisa now has
    total = total_spoons + total_teaspoons
    result = total
    return result

print(solution())
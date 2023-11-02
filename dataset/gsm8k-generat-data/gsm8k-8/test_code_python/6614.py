def solution():
    # Define the number of snakes and eggs
    num_snakes = 3
    num_eggs_per_snake = 2
    total_eggs = num_snakes * num_eggs_per_snake

    # Calculate the total amount earned from regular baby snakes
    regular_baby_snakes = total_eggs - 1
    regular_earnings = regular_baby_snakes * 250

    # Calculate the earnings from the super rare baby snake
    rare_earnings = 4 * 250

    # Calculate the total earnings
    total_earnings = regular_earnings + rare_earnings
    result = total_earnings
    return result

print(solution())
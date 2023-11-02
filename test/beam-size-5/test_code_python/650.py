def solution():
    
    # Define the number of guests and deviled egg halves needed
    guests = 16
    egg_halves_needed = 2

    # Calculate the total number of egg halves needed
    total_egg_halves = egg_halves_needed * guests

    # Calculate the number of dozens of eggs needed
    dozens_of_eggs = total_egg_halves / 12

    # Display the number of dozens of eggs needed
    result = dozens_of_eggs
    return result

print(solution())
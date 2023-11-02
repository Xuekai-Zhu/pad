def solution():
    initial_female_bunnies = 30  # Marlon had 30 female baby bunnies in his hutch
    mature_bunnies = initial_female_bunnies * (2/5)  # Marlon gave 2/5 of the mature female bunnies to Rodney
    remaining_bunnies = initial_female_bunnies - mature_bunnies  # Calculate the remaining female bunnies in Marlon's hutch
    new_born_bunnies = remaining_bunnies * 2  # Each remaining female bunny gave birth to 2 kittens

    # Calculate the total number of bunnies Marlon has in his hutch now
    total_bunnies = mature_bunnies + remaining_bunnies + new_born_bunnies
    result = total_bunnies
    return result

print(solution())
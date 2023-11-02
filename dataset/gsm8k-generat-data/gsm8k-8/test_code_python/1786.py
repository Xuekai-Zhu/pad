def solution():
    # Calculate the total number of eggs
    total_eggs = 1

    # Calculate the number of blue and purple eggs
    blue_eggs = (4/5) * total_eggs
    purple_eggs = (1/5) * total_eggs

    # Calculate the number of purple eggs with five pieces of candy each
    purple_five_candy_eggs = (1/2) * purple_eggs

    # Calculate the number of blue eggs with four pieces of candy each
    blue_four_candy_eggs = (1/4) * blue_eggs

    # Calculate the total number of eggs with five pieces of candy each
    eggs_five_candy = purple_five_candy_eggs + blue_four_candy_eggs

    # Calculate the percentage chance of getting an egg with five pieces of candy
    chance_five_candy = (eggs_five_candy / total_eggs) * 100
    result = chance_five_candy
    return result

print(solution())
def solution():
    # Calculate the number of blue and purple eggs
    blue_eggs = (4/5) * 100  # assuming there are 100 Easter eggs
    purple_eggs = (1/5) * 100

    # Calculate the number of blue and purple eggs with 5 pieces of candy
    blue_with_5_candy = (1/4) * blue_eggs
    purple_with_5_candy = (1/2) * (1/5) * purple_eggs

    # Calculate the total number of eggs with 5 pieces of candy
    total_with_5_candy = blue_with_5_candy + purple_with_5_candy

    # Calculate the percentage chance of getting an egg with 5 pieces of candy
    percentage_chance = (total_with_5_candy / 100) * 100
    result = percentage_chance
    return result

print(solution())
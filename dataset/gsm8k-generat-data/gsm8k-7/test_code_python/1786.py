def solution():
    blue_eggs = 4/5
    purple_eggs = 1/5

    # Calculate the proportion of purple eggs with 5 pieces of candy
    purple_eggs_with_5_candy = 1/2

    # Calculate the proportion of blue eggs with 1/4 having 5 pieces of candy
    blue_eggs_with_5_candy = 1/4 * blue_eggs

    # Calculate the proportion of all eggs with 5 pieces of candy
    total_eggs_with_5_candy = (purple_eggs * purple_eggs_with_5_candy) + (blue_eggs * blue_eggs_with_5_candy)

    # Calculate the percentage chance of getting an egg with 5 pieces of candy
    percentage_chance = total_eggs_with_5_candy * 100
    result = percentage_chance
    return result

print(solution())
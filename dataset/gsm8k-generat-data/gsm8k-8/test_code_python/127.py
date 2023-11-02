def solution():
    # Define the meows per minute for each cat
    cat1_meows = 3
    cat2_meows = 2 * cat1_meows
    cat3_meows = cat2_meows / 3

    # Calculate the total meows over 5 minutes for each cat
    cat1_total = cat1_meows * 5
    cat2_total = cat2_meows * 5
    cat3_total = cat3_meows * 5

    # Calculate the combined total of meows
    total_meows = cat1_total + cat2_total + cat3_total
    result = total_meows
    return result

print(solution())
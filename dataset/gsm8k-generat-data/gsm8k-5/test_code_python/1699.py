def solution():
    total_flowers = 105  # The garden has 105 flowers in total
    orange_flowers = 10  # There are 10 orange flowers
    red_flowers = 2 * orange_flowers  # There are twice as many red flowers as orange
    yellow_flowers = red_flowers - 5  # There are five fewer yellow flowers than red

    # Calculate the number of pink and purple flowers
    other_flowers = total_flowers - orange_flowers - red_flowers - yellow_flowers

    # Since the pink and purple flowers have the same amount, we can divide the remaining flowers in half
    pink_and_purple = other_flowers / 2
    result = pink_and_purple
    return result

print(solution())
def solution():
    total_veggies = 280  # Barry will use 280 pieces of vegetables in total

    # Let x be the number of cucumbers
    x = total_veggies / 4  # There are 4 pieces of vegetables for each pair of cucumbers and tomatoes

    # Let y be the number of tomatoes
    y = 3 * x  # There are thrice as many tomatoes as cucumbers

    # Calculate the number of cucumbers needed for the salad
    cucumbers_needed = x
    result = cucumbers_needed
    return result

print(solution())
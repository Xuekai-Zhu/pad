def solution():
    flowers_per_dozen = 12  # Each dozen contains 12 flowers
    free_flowers_per_dozen = 2  # For every dozen bought, 2 free flowers are given
    total_dozen = 3  # Maria wants to buy 3 dozens of flowers

    # Calculate the total number of flowers Maria will receive, including the free ones
    total_flowers = (flowers_per_dozen + free_flowers_per_dozen) * total_dozen

    result = total_flowers
    return result

print(solution())
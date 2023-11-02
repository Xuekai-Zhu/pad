def solution():
    # Define the percentage of other elements in the moon
    moon_other = 30

    # Calculate the percentage of other elements in Mars
    mars_other = 150 / 2

    # Calculate the total weight of the moon
    moon_weight = 100 / moon_other * mars_other
    result = moon_weight
    return result

print(solution())
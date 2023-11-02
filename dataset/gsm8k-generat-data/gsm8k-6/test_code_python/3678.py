def solution():
    # Calculate the number of years it takes for the tree to grow to 23 feet tall
    target_height = 23
    current_height = 5
    growth_rate = 3
    years = (target_height - current_height) / growth_rate

    # Determine the age of the tree when it reaches 23 feet tall
    age = years + 1  # add 1 to include the first year the tree was planted
    result = age
    return result

print(solution())
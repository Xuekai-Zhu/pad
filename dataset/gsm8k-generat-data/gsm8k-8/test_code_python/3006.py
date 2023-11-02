def solution():
    # Define the total number of flavors and Gretchen's previous tastings
    total_flavors = 100
    previous_tastings = (1/4) * total_flavors + 2 * (1/4) * total_flavors

    # Calculate how many more flavors Gretchen needs to try
    remaining_flavors = total_flavors - previous_tastings
    result = remaining_flavors
    return result

print(solution())
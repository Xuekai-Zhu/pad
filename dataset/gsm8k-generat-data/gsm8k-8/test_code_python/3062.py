def solution():
    # Define the amount of vegetables and broth in one serving
    vegetables_per_serving = 1
    broth_per_serving = 2.5

    # Calculate the total amount of vegetables and broth needed for 8 servings
    total_vegetables = vegetables_per_serving * 8
    total_broth = broth_per_serving * 8
    total_pints = (total_vegetables + total_broth) / 2

    # Convert the total amount to pints
    result = total_pints
    return result

print(solution())
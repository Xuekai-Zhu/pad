def solution():
    # Define the number of cherry sodas as x
    x = 24 / 3

    # Define the number of orange pops as 2*x
    orange_pop = 2*x

    # Verify that the total number of cans equals 24
    total_cans = x + orange_pop
    if total_cans == 24:
        result = x
    else:
        result = "Error: Total number of cans does not equal 24"
    return result

print(solution())
def solution():
    # Define the number of haircuts needed for a free one
    haircuts_for_free = 14

    # Calculate the total number of haircuts Tammy has paid for
    total_paid_haircuts = (5 + 1) * haircuts_for_free - 5

    # Calculate the number of haircuts Tammy has gotten, including free ones
    total_haircuts = total_paid_haircuts + 5

    result = total_haircuts
    return result

print(solution())
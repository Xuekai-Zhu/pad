def solution():
    
    # Define the initial funding and the number of months
    INITIAL_FRIEND = 100000
    MONTHS_FIRST_FIVE = 5

    # Calculate the total number of months
    total_months = MONTHS_FIRST_FIVE * MONTHS_FIRST_FIVE

    # Calculate the total funding for the first 5 months
    first_four_months_funding = INITIAL_FRIEND * 10 * MONTHS_FIRST_FIVE

    # Calculate the total funding for the remaining months
    remaining_funding = INITIAL_FRIEND * 10 * MONTHS_FIRST_FIVE * 1.5

    # Calculate the total cost of the research
    total_cost = first_four_months_funding + remaining_funding

    # Display the total cost
    result = total_cost
    return result

print(solution())
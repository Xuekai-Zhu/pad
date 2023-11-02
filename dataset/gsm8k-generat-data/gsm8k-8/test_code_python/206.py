def solution():
    # Define the variables
    lions_at_first = 0
    lion_cubs_born_per_month = 5
    lions_die_per_month = 1

    # Calculate the number of lions after 1 year
    lions_after_one_year = 148

    # Calculate the number of months in 1 year
    months_in_one_year = 12

    # Use a loop to calculate the number of lions at first
    for i in range(months_in_one_year):
        # Calculate the number of lions at the end of each month
        lions_at_end_of_month = lions_at_first + lion_cubs_born_per_month - lions_die_per_month

        # Update the number of lions at first with the number of lions at the end of the current month
        lions_at_first = lions_at_end_of_month

    # Return the number of lions at first
    result = lions_at_first
    return result

print(solution())
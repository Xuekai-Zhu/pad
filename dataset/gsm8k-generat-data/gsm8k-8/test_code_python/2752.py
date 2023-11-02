def solution():
    # Define the amount spent on the library
    library_spending_percentage = 0.15
    library_spending = 3000

    # Calculate the amount spent on public parks
    parks_spending_percentage = 0.24
    parks_spending = library_spending / library_spending_percentage * parks_spending_percentage

    # Calculate the total amount spent
    total_spending = library_spending + parks_spending

    # Calculate the amount left in the annual budget
    remaining_budget = 1 - (total_spending / library_spending_percentage)
    result = remaining_budget
    return result

print(solution())
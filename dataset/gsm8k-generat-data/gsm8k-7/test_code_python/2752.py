def solution():
    library_percentage = 0.15
    library_spending = 3000

    parks_percentage = 0.24

    # Calculate the total percentage of the budget spent on items other than the library and parks
    other_percentage = 1 - library_percentage - parks_percentage

    # Calculate the total amount of the budget spent on items other than the library and parks
    other_spending = (library_spending / library_percentage) * other_percentage

    # Calculate the total annual budget
    total_budget = library_spending / library_percentage

    # Calculate the amount left of the annual budget
    amount_left = total_budget - library_spending - other_spending
    result = amount_left
    return result

print(solution())
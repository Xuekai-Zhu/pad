def solution():
    """The town of Centerville spends 15% of its annual budget on its public library. Centerville spent $3,000 on its public library and 24% on the public parks. How much is left of the annual budget?"""
    # Define the percentage of the annual budget spent on the library and parks
    LIBRARY_PERCENTAGE = 0.15
    PARKS_PERCENTAGE = 0.24

    # Define the amount spent on the library and parks
    library_spending = 3000
    parks_spending = library_spending / PARKS_PERCENTAGE * LIBRARY_PERCENTAGE

    # Calculate the total annual budget
    total_budget = (library_spending + parks_spending) / (LIBRARY_PERCENTAGE + PARKS_PERCENTAGE)

    # Calculate the remaining budget
    remaining_budget = total_budget - library_spending - parks_spending

    # Display the remaining budget
    result = remaining_budget
    return result

print(solution())
def solution():
    library_percentage = 0.15  # Centerville spends 15% of its budget on the library
    park_percentage = 0.24  # Centerville spends 24% of its budget on the parks
    library_budget = 3000  # Centerville spent $3000 on the library

    # Calculate the total annual budget
    total_budget = library_budget / library_percentage

    # Calculate the amount spent on public parks
    park_budget = total_budget * park_percentage

    # Calculate the amount left of the annual budget
    remaining_budget = total_budget - library_budget - park_budget
    result = remaining_budget
    return result

print(solution())
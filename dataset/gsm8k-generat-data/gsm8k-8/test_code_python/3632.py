def solution():
    # Calculate the total number of pages
    total_pages = 2 * 50

    # Convert the total cost to cents
    total_cost = 5 * 100

    # Calculate the cost per page in cents
    cost_per_page = total_cost / total_pages

    # Round the result to 2 decimal places and convert back to dollars
    result = round(cost_per_page, 2)
    return result

print(solution())
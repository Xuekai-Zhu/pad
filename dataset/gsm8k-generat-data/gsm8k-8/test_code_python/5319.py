def solution():
    # Define the number of adults and children
    num_adults = 400
    num_children = 200

    # Set up the equation for the total amount collected
    total_collected = (2 * adult_price * num_adults) + (child_price * num_children)
    # Solve for adult_price
    adult_price = (total_collected - (child_price * num_children)) / (2 * num_adults)

    result = adult_price
    return result

print(solution())
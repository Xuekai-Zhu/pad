def solution():
    
    # Define the number of croissants needed
    croissants_needed = 6 * 12

    # Calculate the amount of butter needed
    butter_needed = croissants_needed / 6

    # Calculate the discounted price of the butter
    discounted_price = butter_needed / 2

    # Calculate the total cost of the butter
    total_cost = discounted_price * 6

    # Display the total cost
    result = total_cost
    return result

print(solution())
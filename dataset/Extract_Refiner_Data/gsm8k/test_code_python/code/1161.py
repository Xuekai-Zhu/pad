def solution():
    
    # Define the number of apartments in each complex
    apartments_first_two = 200
    apartments_last_two = apartments_first_two * 1.6

    # Calculate the total number of apartments collected in a week
    total_apartments = apartments_first_two + apartments_last_two

    # Calculate the total amount of money John makes in a week
    total_money = total_apartments * 0.40 * 3

    # Display the total amount of money John makes in a week
    result = total_money
    return result

print(solution())
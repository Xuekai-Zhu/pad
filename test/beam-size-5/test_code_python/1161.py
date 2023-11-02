def solution():
    
    # Define the number of apartments in the first two complexes
    apartments_first_two = 200

    # Calculate the number of apartments in the last two complexes
    apartments_last_two = apartments_first_two * 1.6

    # Calculate the total number of apartments collected in a week
    total_apartments = apartments_first_two + apartments_last_two

    # Calculate the total amount of money collected in a week
    total_money = total_apartments * 0.40

    # Display the total amount of money collected in a week
    result = total_money
    return result

print(solution())
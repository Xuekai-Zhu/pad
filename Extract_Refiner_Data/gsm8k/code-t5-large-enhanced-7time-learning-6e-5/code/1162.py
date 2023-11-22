def solution():
    
    # Define the initial number of fruits produced by each year
    initial_5_years = 50
    initial_6_years = 3 * initial_5_years
    initial_7_years = 7 * initial_5_years
    initial_8_years = 10 * initial_5_years - 200

    # Calculate the total number of fruits produced
    total_fruits = initial_5_years + initial_6_years + initial_7_years + initial_8_years

    # Display the total number of fruits produced
    result = total_fruits
    return result

print(solution())
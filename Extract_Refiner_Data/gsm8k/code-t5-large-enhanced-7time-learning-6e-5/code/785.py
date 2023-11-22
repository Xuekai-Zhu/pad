def solution():
    
    # Define the temperature limit and the temperature burns per log
    temp_limit = 32
    wood_burn_per_log = 5

    # Calculate the total temperature and wood burns
    total_temp = 45 + 33
    wood_burned = total_temp - temp_limit

    # Calculate the number of logs Carson needs to burn to ensure the house is freezing
    num_logs = wood_burned / wood_burn_per_log

    # Display the number of logs Carson needs to burn
    result = num_logs
    return result

print(solution())
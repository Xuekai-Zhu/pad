def solution():
    # Define the initial height and final height
    initial_height = 20
    final_height = 80

    # Calculate the total growth over the year
    total_growth = final_height - initial_height

    # Calculate the monthly growth rate
    monthly_growth_rate = total_growth / 12
    result = monthly_growth_rate
    return result

print(solution())
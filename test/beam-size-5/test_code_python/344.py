def solution():
    
    # Define the number of tractors sold and the earnings per tractor
    tractors_sold = 10
    tractor_earnings = 100

    # Define the number of silos sold and the earnings per silo
    silos_sold = 5
    silo_earnings = 220

    # Calculate the total earnings for the day
    total_earnings = (tractors_sold * tractor_earnings) + (silos_sold * silo_earnings)

    # Calculate the percentage increase in earnings per day
    percentage_increase = (silo_earnings / total_earnings) * 100

    # return the result
    result = percentage_increase
    return result

print(solution())
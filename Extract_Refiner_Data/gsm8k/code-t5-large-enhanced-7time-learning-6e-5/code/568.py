def solution():
    
    # Define the number of roses gained per week
    roses_per_week = 40

    # Define the number of roses ordered per week
    roses_per_week1 = 20
    roses_per_week2 = 15
    roses_per_week3 = 30

    # Calculate the total number of roses ordered per week
    total_roses_per_week = roses_per_week1 + roses_per_week2 + roses_per_week3

    # Calculate the number of roses that Ford lacks to supply each shop per week
    roses_lack_per_week = total_roses_per_week - roses_per_week

    # Calculate the number of roses that Ford lacks to supply each shop per month
    roses_lack_per_month = roses_lack_per_week * 4

    # Display the number of roses that Ford lacks to supply each shop per month
    result = roses_lack_per_month
    return

print(solution())
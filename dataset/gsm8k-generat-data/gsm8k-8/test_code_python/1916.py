def solution():
    # Define the hourly rates and amount of time worked for each family
    rate1 = 15
    hours1 = 7
    rate2 = 18
    hours2 = 6
    rate3 = 20
    hours3 = 3

    # Calculate the amount earned for each family
    earnings1 = rate1 * hours1
    earnings2 = rate2 * hours2
    earnings3 = rate3 * hours3

    # Calculate Layla's total earnings
    total_earnings = earnings1 + earnings2 + earnings3
    result = total_earnings
    return result

print(solution())
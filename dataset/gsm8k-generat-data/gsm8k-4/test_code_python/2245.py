def solution():
    """There are 100 lions in Londolozi at first. If lion cubs are born at the rate of 5 per month and lions die at the rate of 1 per month, how many lions will there be in Londolozi after 1 year?"""
    # Define the initial number of lions
    lions = 100

    # Define the number of months in a year
    months = 12

    # Calculate the net change in lions each month
    net_change = 5 - 1

    # Calculate the total change in lions over the year
    total_change = net_change * months

    # Calculate the final number of lions
    final_lions = lions + total_change

    # return the result
    result = final_lions
    return result

print(solution())
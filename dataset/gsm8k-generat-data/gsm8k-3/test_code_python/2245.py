def solution():
    """There are 100 lions in Londolozi at first. If lion cubs are born at the rate of 5 per month and lions die at the rate of 1 per month, how many lions will there be in Londolozi after 1 year?"""
    # Define the initial number of lions
    INITIAL_LIONS = 100

    # Calculate the number of lions after each month
    lions = INITIAL_LIONS
    for i in range(12):
        lions += 4 # 5 cubs born, 1 lion dies
    result = lions
    return result

print(solution())
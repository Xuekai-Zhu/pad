def solution():
    
    # Define the number of packages completed per hour and the pay rate per package
    PACKAGES_PER_HOUR = 50 - 10
    PAY_RATE_PER_PACKAGE = 0.20

    # Calculate the total number of packages completed in 8 hours
    total_packages = PACKAGES_PER_HOUR * 8

    # Calculate the total pay earned in 8 hours
    total_pay = total_packages * PAY_RATE_PER_PACKAGE

    # Display the total pay earned
    result = total_pay
    return result

print(solution())
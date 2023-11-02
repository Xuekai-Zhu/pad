def solution():
    """Xavier runs three times as many miles as Katie, who runs 4 times as many miles as Cole. If Xavier runs 84 miles, how many miles does Cole run?"""
    # Define the number of miles run by Xavier
    xavier_miles = 84
    
    # Calculate the number of miles run by Katie using the fact that she runs 1/3 as many miles as Xavier
    katie_miles = xavier_miles / 3
    
    # Calculate the number of miles run by Cole using the fact that Katie runs 4 times as many miles as Cole
    cole_miles = katie_miles / 4
    
    result = cole_miles
    return result

print(solution())
def solution():
    """Matt orders 15 pounds of beef.  He cuts that into 12-ounce steaks.  How many steaks does he get?"""
    # Define the weight of the beef in ounces
    beef_weight = 15 * 16

    # Divide the weight of the beef by the weight of each steak to get the number of steaks
    num_steaks = beef_weight / 12

    # Display the number of steaks
    result = num_steaks
    return result

print(solution())
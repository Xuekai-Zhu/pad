def solution():
    """Matthew asked his children how many hotdogs they wanted for dinner.  Both Ella and Emma agreed they wanted 2 hotdogs each.  Luke said he could eat twice the amount of hotdogs as his sisters while Hunter said he could only eat 1 and half times the total amount of his sisters.  How many hotdogs did Matthew need to cook?"""
    # Define the number of hotdogs each child wants
    ella_hotdogs = 2
    emma_hotdogs = 2
    luke_hotdogs = ella_hotdogs * 2
    hunter_hotdogs = (ella_hotdogs + emma_hotdogs) * 1.5

    # Calculate the total number of hotdogs needed
    total_hotdogs = ella_hotdogs + emma_hotdogs + luke_hotdogs + hunter_hotdogs

    # Display the total number of hotdogs
    result = total_hotdogs
    return result

print(solution())
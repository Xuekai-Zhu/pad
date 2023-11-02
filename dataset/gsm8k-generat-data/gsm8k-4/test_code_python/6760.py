def solution():
    """Matthew asked his children how many hotdogs they wanted for dinner. Both Ella and Emma agreed they wanted 2 hotdogs each. 
    Luke said he could eat twice the amount of hotdogs as his sisters while Hunter said he could only eat 1 and half times the total amount of his sisters. 
    How many hotdogs did Matthew need to cook?"""
    # Calculate the total number of hotdogs Ella and Emma wanted
    ella_emma_hotdogs = 2 + 2

    # Calculate the number of hotdogs Luke wanted
    luke_hotdogs = ella_emma_hotdogs * 2

    # Calculate the number of hotdogs Hunter wanted
    hunter_hotdogs = ella_emma_hotdogs * 1.5

    # Calculate the total number of hotdogs needed
    total_hotdogs = ella_emma_hotdogs + luke_hotdogs + hunter_hotdogs

    # Return the result
    result = total_hotdogs
    return result

print(solution())
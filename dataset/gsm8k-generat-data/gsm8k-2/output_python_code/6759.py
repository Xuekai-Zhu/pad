def solution():
    """Matthew asked his children how many hotdogs they wanted for dinner. Both Ella and Emma agreed they wanted 2 hotdogs each. Luke said he could eat twice the amount of hotdogs as his sisters while Hunter said he could only eat 1 and half times the total amount of his sisters. How many hotdogs did Matthew need to cook?"""
    ella_and_emma = 2 + 2
    luke = ella_and_emma * 2
    hunter = ella_and_emma * 1.5
    total_hotdogs = ella_and_emma + luke + hunter
    result = total_hotdogs
    return result

print(solution())
def solution():
    """Matthew asked his children how many hotdogs they wanted for dinner. Both Ella and Emma agreed they wanted 2 hotdogs each. Luke said he could eat twice the amount of hotdogs as his sisters while Hunter said he could only eat 1 and half times the total amount of his sisters. How many hotdogs did Matthew need to cook?"""
    ella_hotdogs = 2
    emma_hotdogs = 2
    luke_hotdogs = 2 * 2
    total_sisters_hotdogs = ella_hotdogs + emma_hotdogs
    hunter_hotdogs = 1.5 * total_sisters_hotdogs
    total_hotdogs = ella_hotdogs + emma_hotdogs + luke_hotdogs + hunter_hotdogs
    result = total_hotdogs
    return result

print(solution())
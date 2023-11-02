def solution():
    """Rita hand-picks Junebugs off of her plants every summer. On Monday, she removed 39 Junebugs. On both Tuesday and Wednesday, she removed twice as many Junebugs as she did on Monday. Thursday she removed 48 and on Friday she removed 57. What is the average number of Junebugs that she removes per day?"""
    monday_junebugs = 39
    tuesday_junebugs = monday_junebugs * 2
    wednesday_junebugs = tuesday_junebugs * 2
    thursday_junebugs = 48
    friday_junebugs = 57
    total_junebugs = monday_junebugs + tuesday_junebugs + wednesday_junebugs + thursday_junebugs + friday_junebugs
    days = 5
    avg_junebugs = total_junebugs / days
    result = avg_junebugs
    
    return result

print(solution())
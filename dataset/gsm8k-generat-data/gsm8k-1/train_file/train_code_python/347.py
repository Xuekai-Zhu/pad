def solution():
    """Brian can only hold his breath underwater for 10 seconds. He wants to get better, so he starts practicing. 
    After a week, he's doubled the amount of time he can do it. After another week, he's doubled it again from the previous week. 
    The final week, he's increased it by 50% from the previous week. How long can Brian hold his breath for now?"""
    
    initial_time = 10
    week1_time = initial_time * 2
    week2_time = week1_time * 2
    week3_time = week2_time * 1.5
    total_time = initial_time + week1_time + week2_time + week3_time
    result = total_time
    
    return result

print(solution())
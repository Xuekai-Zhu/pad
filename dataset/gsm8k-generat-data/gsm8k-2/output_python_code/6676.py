def solution():
    """Justin needs to collect one flower for each classmate that is in his 2nd-grade class. It takes him on average 10 minutes to find a flower he likes. He has been gathering for 2 hours. Assuming he has lost 3 of the flowers he initially gathered, how many more minutes does he need to look if he has 30 classmates?"""
    classmates = 30
    flowers_needed = classmates
    time_per_flower = 10
    total_time = 120 # 2 hours in minutes
    flowers_lost = 3
    flowers_collected = flowers_needed + flowers_lost
    time_spent = flowers_collected * time_per_flower
    remaining_time = total_time - time_spent
    result = remaining_time
    return result

print(solution())
def solution():
    """Brian can only hold his breath underwater for 10 seconds. He wants to get better, so he starts practicing. After a week, he's doubled the amount of time he can do it. After another week, he's doubled it again from the previous week. The final week, he's increased it by 50% from the previous week. How long can Brian hold his breath for now?"""
    starting_time = 10
    first_week_time = starting_time * 2
    second_week_time = first_week_time * 2
    third_week_time = second_week_time * 1.5
    total_time = starting_time + first_week_time + second_week_time + third_week_time
    result = total_time
    return result

print(solution())
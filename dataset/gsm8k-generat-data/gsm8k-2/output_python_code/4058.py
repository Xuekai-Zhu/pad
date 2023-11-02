def solution():
    """Mike began to train to play basketball every day for a tournament. One day he plays a maximum of 2 hours. After a week of training, he increased the maximum time to 3 hours. How many hours did Mike train during the first two weeks?"""
    first_week_hours = 0
    second_week_hours = 0
    for i in range(14):
        if i < 7:
            first_week_hours += 2
        else:
            second_week_hours += 3
    total_hours = first_week_hours + second_week_hours
    result = total_hours
    return result

print(solution())
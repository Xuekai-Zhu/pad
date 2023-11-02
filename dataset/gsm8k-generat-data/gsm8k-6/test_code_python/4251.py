def solution():
    # Calculate the total distance Carly ran in the first 2 weeks
    total_distance = 2 + (2*2+3)  

    # Calculate the distance she ran in the third week
    third_week_distance = (9/7) * (2*2+3)  

    # Calculate the total distance she ran in the first 3 weeks
    total_distance += third_week_distance

    # Calculate the distance she ran in the fourth week
    fourth_week_distance = third_week_distance - 5  

    result = fourth_week_distance
    return result

print(solution())
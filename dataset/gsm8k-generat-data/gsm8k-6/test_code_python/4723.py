def solution():
    # Calculate the total distance walked by Cary
    total_distance = 3  

    # Calculate the total calories burned by Cary
    calories_burned = total_distance * 150  

    # Calculate the net calorie deficit of Cary
    net_calorie_deficit = 200 - calories_burned  

    # Make sure the result is positive
    result = abs(net_calorie_deficit)
    return result

print(solution())
def solution():
    apple_pies_per_day = 4  # Steve bakes 4 apple pies on Mon, Wed, Fri
    cherry_pies_per_day = 3  # Steve bakes 3 cherry pies on Tue, Thu
    days_per_week = 5  # Steve bakes pies on 5 days per week

    # Calculate the total number of apple pies Steve bakes per week
    total_apple_pies = apple_pies_per_day * 3  # 3 days of apple pies per week

    # Calculate the total number of cherry pies Steve bakes per week
    total_cherry_pies = cherry_pies_per_day * 2  # 2 days of cherry pies per week

    # Calculate the difference between the total number of apple and cherry pies Steve bakes per week
    difference = total_apple_pies - total_cherry_pies
    result = difference
    return result

print(solution())
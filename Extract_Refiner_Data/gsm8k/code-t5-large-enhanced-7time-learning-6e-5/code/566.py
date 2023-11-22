def solution():
    
    # Define the initial amount of money Peter has
    initial_money = 70

    # Calculate the amount of money Peter spends on action figures each day
    daily_spending = initial_money / 7
    daily_wooden = 5
    daily_wednesday = 5
    daily_plastic = 2

    # Calculate the total amount spent on action figures for the week
    total_spending = (daily_spending * 7) + (daily_wooden * 7) + (daily_plastic * 7)

    # Calculate the total number of action figures Peter will have by the end of the week
    total_figures = total_spending + total_wooden + total_plastic

    # return the result
    result = total_figures
    return result

print(solution())
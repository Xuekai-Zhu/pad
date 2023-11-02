def solution():
    # Calculate the total number of windows in Lucas' house
    total_windows = 3 * 3  # each floor has 3 windows, Lucas lives in a 3-story house

    # Calculate the amount of money Lucas will lose for not finishing the job in time
    money_lost = (1/3) * ((6-1)//3)  # subtract $1 for every 3 days that pass without Lucas finishing the job

    # Calculate the total amount of money Lucas will earn
    total_money = 2 * total_windows - money_lost

    result = total_money
    return result

print(solution())
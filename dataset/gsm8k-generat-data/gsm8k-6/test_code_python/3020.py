def solution():
    # Calculate the total amount of fish caught by Erica today
    today_fish = 2 * 80

    # Calculate the total amount of fish caught by Erica in the past four months, including today
    total_fish = 80 + today_fish

    # Calculate the total amount of money earned by Erica in the past four months, including today
    total_money = total_fish * 20

    result = total_money
    return result

print(solution())
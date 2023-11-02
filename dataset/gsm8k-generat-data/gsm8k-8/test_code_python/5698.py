def solution():
    # Define the initial amount of money and the cost of the vacuum cleaner
    initial_money = 20
    vacuum_cleaner_cost = 120

    # Define the amount of money Daria puts in the piggy bank each week
    weekly_contribution = 10

    # Calculate the number of weeks it will take to reach the vacuum cleaner cost
    weeks_needed = (vacuum_cleaner_cost - initial_money) / weekly_contribution
    result = int(weeks_needed)
    return result

print(solution())
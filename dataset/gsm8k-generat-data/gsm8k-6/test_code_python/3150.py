def solution():
    # Calculate the total amount of money Percy will have
    total_money = 200 + 150  # $200 from birthday, $150 from Christmas
    remaining_money = 500 - total_money  # Calculate the remaining amount of money needed
    games_needed = remaining_money / 7.5  # Calculate how many games Percy needs to sell to reach his goal
    result = games_needed
    return result

print(solution())
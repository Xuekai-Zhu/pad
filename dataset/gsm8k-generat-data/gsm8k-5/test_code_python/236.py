def solution():
    starting_money = 5000  # Jake has $5000
    motorcycle_cost = 2800  # Jake spends $2800 on a new motorcycle
    money_left_after_motorcycle = starting_money - motorcycle_cost

    # Jake spends half of what's left on a concert ticket
    money_spent_on_concert = money_left_after_motorcycle / 2
    money_left_after_concert = money_left_after_motorcycle - money_spent_on_concert

    # Jake then loses a fourth of what he has left
    money_lost = money_left_after_concert / 4
    money_left = money_left_after_concert - money_lost
    result = money_left
    return result

print(solution())
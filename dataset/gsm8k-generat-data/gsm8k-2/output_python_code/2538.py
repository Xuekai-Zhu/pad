def solution():
    """Florida is starting a promotion where every car that arrives gets one orange per passenger. A family of 4 arrives and gets their oranges. They had planned to stop for a snack later where they would spend $15 in total, but now that they have the oranges they don't have to buy them at the stop. When they get to the stop they see that the oranges would've cost $1.5 each. What percentage of the money they planned to spend did they save instead?"""
    passengers = 4
    oranges_received = passengers
    planned_spending = 15
    orange_cost = 1.5
    actual_spending = planned_spending - (oranges_received * orange_cost)
    saved_money = planned_spending - actual_spending
    percentage_saved = (saved_money / planned_spending) * 100
    result = percentage_saved
    return result

print(solution())
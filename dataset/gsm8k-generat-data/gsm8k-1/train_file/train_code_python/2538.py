def solution():
    """Florida is starting a promotion where every car that arrives gets one orange per passenger. A family of 4 arrives and gets their oranges. They had planned to stop for a snack later where they would spend $15 in total, but now that they have the oranges they don't have to buy them at the stop. When they get to the stop they see that the oranges would've cost $1.5 each. What percentage of the money they planned to spend did they save instead?"""
    num_passengers = 4
    oranges_per_passenger = 1
    total_oranges = num_passengers * oranges_per_passenger
    cost_per_orange = 1.5
    money_saved = total_oranges * cost_per_orange
    percent_saved = (money_saved / 15) * 100
    result = percent_saved
    return result

print(solution())
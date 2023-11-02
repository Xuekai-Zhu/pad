def solution():
    """Stetson made a bet with Alec that he would give up $10 for each orange he eats. While at the farm, Stetson ate 2/5 of the oranges they picked. If they picked 60 oranges, calculate the total amount of money Stetson gave up?"""
    oranges_picked = 60
    percent_oranges_eaten = 2/5
    oranges_eaten = percent_oranges_eaten * oranges_picked
    cost_per_orange = 10
    total_cost = oranges_eaten * cost_per_orange
    result = total_cost
    return result

print(solution())
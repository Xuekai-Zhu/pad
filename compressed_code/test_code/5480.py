def solution():
    
    goal_money = 200
    raised_money = 0
    raised_money += 20 * 2  
    raised_money += 10 * 8  
    raised_money += 5 * 10  
    remaining_money = goal_money - raised_money
    result = remaining_money
    return result

print(solution())
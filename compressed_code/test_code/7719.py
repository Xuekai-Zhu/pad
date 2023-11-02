def solution():
    
    goal_amount = 750
    bronze_count = 10
    silver_count = 7
    gold_count = 1
    bronze_amount = 25
    silver_amount = 50
    gold_amount = 100
    current_amount = bronze_amount * bronze_count + silver_amount * silver_count + gold_amount * gold_count
    remaining_amount = goal_amount - current_amount
    result = remaining_amount
    
    return result

print(solution())
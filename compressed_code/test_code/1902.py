def solution():
    
    bronze_donation = 25
    silver_donation = 50
    gold_donation = 100
    bronze_count = 10
    silver_count = 7
    gold_count = 1
    total_raised = (bronze_count * bronze_donation) + (silver_count * silver_donation) + (gold_count * gold_donation)
    remaining_goal = 750 - total_raised
    result = remaining_goal
    return result

print(solution())
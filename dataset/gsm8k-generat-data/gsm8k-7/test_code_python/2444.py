def solution():
    goal = 750
    bronze_price = 25
    silver_price = 50
    gold_price = 100
    bronze_families = 10
    silver_families = 7
    gold_families = 1

    # Calculate the total amount already raised
    total_raised = (bronze_price * bronze_families) + (silver_price * silver_families) + (gold_price * gold_families)

    # Calculate how much more is needed to reach the goal
    remaining_goal = goal - total_raised
    result = remaining_goal
    return result

print(solution())
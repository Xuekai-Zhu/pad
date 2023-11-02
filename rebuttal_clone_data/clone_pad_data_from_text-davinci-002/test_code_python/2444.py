def solution():
    total_needed = 750
    bronze_families = 10
    silver_families = 7
    gold_families = 1
    bronze_amount = 25 * bronze_families
    silver_amount = 50 * silver_families
    gold_amount = 100 * gold_families
    total_raised = bronze_amount + silver_amount + gold_amount
    money_needed = total_needed - total_raised
    result = money_needed
    return result

print(solution())
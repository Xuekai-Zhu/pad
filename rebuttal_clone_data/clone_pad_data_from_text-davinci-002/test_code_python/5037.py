def solution():
    silver_watches = 20
    bronze_watches = silver_watches * 3
    total_watches = silver_watches + bronze_watches
    gold_watches = total_watches / 10
    total_after_purchase = total_watches + gold_watches
    result = total_after_purchase
    return result

print(solution())
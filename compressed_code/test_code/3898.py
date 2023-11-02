def solution():
    
    silver_watches = 20
    bronze_watches = 3 * silver_watches
    total_watches = silver_watches + bronze_watches
    gold_watches = int(total_watches * 0.1)
    total_watches += gold_watches
    result = total_watches
    return result

print(solution())
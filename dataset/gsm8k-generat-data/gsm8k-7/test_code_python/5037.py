def solution():
    silver_watches = 20
    bronze_watches = silver_watches * 3
    total_watches = silver_watches + bronze_watches
    gold_watches = int(total_watches * 0.1)  # round down to integer

    total_watches += gold_watches
    result = total_watches
    return result

print(solution())
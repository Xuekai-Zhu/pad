def solution():
    silver_watches = 20  # Julia owns 20 silver watches
    bronze_watches = silver_watches * 3  # Julia owns three times as many bronze watches as silver watches
    total_watches = silver_watches + bronze_watches  # Calculate the total number of watches Julia owns
    gold_watches = round(total_watches * 0.10)  # Julia buys 10% of all the watches she owns in gold

    # Calculate the total number of watches Julia owns after the purchase
    total_watches += gold_watches
    result = total_watches
    return result

print(solution())
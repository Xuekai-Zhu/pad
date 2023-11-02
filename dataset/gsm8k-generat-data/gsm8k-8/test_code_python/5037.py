def solution():
    # Define the number of silver watches and calculate the number of bronze watches
    silver_watches = 20
    bronze_watches = silver_watches * 3

    # Calculate the total number of watches before the gold watch purchase
    total_watches = silver_watches + bronze_watches

    # Calculate the number of gold watches that Julia purchased
    gold_watches = int(total_watches * 0.1)

    # Calculate the total number of watches after the gold watch purchase
    total_watches_after_purchase = total_watches + gold_watches
    result = total_watches_after_purchase
    return result

print(solution())
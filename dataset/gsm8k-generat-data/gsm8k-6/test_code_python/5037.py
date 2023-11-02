def solution():
    # Calculate the number of bronze watches Julia owns
    bronze_watches = 3 * 20  # Julia owns three times as many bronze watches as silver watches

    # Calculate the total number of watches Julia owns before buying gold watches
    total_watches = 20 + bronze_watches

    # Calculate the number of gold watches Julia buys
    gold_watches = round(total_watches * 0.1)

    # Calculate the total number of watches Julia owns after buying gold watches
    total_watches += gold_watches

    result = total_watches
    return result

print(solution())
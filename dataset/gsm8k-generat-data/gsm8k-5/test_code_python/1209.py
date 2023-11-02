def solution():
    num_of_gold_bars = 60  # Jame has 60 bars of gold
    tax_rate = 0.1  # Jame uses 10% of his gold bars to pay for tax

    # Calculate the number of gold bars Jame uses to pay for tax
    tax = num_of_gold_bars * tax_rate
    num_of_gold_bars -= tax

    # Calculate the number of gold bars Jame loses in divorce
    num_of_gold_bars /= 2

    result = num_of_gold_bars
    return result

print(solution())
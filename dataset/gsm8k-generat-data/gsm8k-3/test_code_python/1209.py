def solution():
    """Jame has 60 bars of gold.  He uses 10% of them to pay for tax and then loses half of what is left in divorce.  How many gold bars does he have left?"""
    # Initial number of gold bars
    gold_bars = 60

    # Calculate the number of gold bars used for tax
    tax = gold_bars * 0.1

    # Calculate the number of gold bars left after paying tax
    gold_bars -= tax

    # Calculate the number of gold bars lost in divorce
    gold_bars /= 2

    # Final number of gold bars
    result = gold_bars
    return result

print(solution())
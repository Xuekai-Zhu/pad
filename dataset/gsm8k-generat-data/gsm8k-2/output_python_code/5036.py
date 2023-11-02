def solution():
    """Julia collects old watches. She owns 20 silver watches, and three times as many bronze watches. She decided to buy gold watches to add to her collection, a number that represents 10% of all the watches she owns. How many watches does Julia own after this purchase?"""
    silver_watches = 20
    bronze_watches = 3 * silver_watches
    total_watches = silver_watches + bronze_watches
    gold_watches = int(total_watches * 0.1)
    total_watches += gold_watches
    result = total_watches
    return result

print(solution())
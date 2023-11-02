def solution():
    """Julia collects old watches. She owns 20 silver watches, and three times as many bronze watches. She decided to buy gold watches to add to her collection, a number that represents 10% of all the watches she owns. How many watches does Julia own after this purchase?"""
    # Define the number of silver watches
    silver_watches = 20

    # Define the number of bronze watches (three times the number of silver watches)
    bronze_watches = silver_watches * 3

    # Calculate the total number of watches Julia owns before the purchase
    total_watches = silver_watches + bronze_watches

    # Calculate the number of gold watches Julia will buy (10% of total watches)
    gold_watches = total_watches * 0.1

    # Calculate the new total number of watches Julia owns after the purchase
    new_total_watches = total_watches + gold_watches

    result = new_total_watches
    return result

print(solution())
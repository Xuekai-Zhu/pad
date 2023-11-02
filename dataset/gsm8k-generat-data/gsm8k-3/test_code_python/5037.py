def solution():
    """Julia collects old watches. She owns 20 silver watches, and three times as many bronze watches. She decided to buy gold watches to add to her collection, a number that represents 10% of all the watches she owns. How many watches does Julia own after this purchase?"""
    # Define the number of silver watches owned
    silver_watches = 20

    # Calculate the number of bronze watches owned
    bronze_watches = 3 * silver_watches

    # Calculate the total number of watches owned before the purchase
    total_watches_before = silver_watches + bronze_watches

    # Calculate the number of gold watches to buy
    gold_watches = int(total_watches_before * 0.1)

    # Calculate the total number of watches owned after the purchase
    total_watches_after = total_watches_before + gold_watches

    # Display the total number of watches owned after the purchase
    result = total_watches_after
    return result

print(solution())
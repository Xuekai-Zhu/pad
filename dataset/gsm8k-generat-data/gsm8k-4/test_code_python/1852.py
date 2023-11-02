def solution():
    """Kameron has 100 kangaroos on his large farm; Bert has 20 kangaroos on his farm. In how many more days will Bert have the same number of kangaroos as Kameron does now if he buys kangaroos at the same rate of 2 new kangaroos per day?"""
    # Define the initial number of kangaroos on the farms
    kameron_kangaroos = 100
    bert_kangaroos = 20

    # Define the rate of kangaroo purchase
    kangaroo_purchase_rate = 2

    # Calculate the difference in number of kangaroos
    kangaroo_difference = kameron_kangaroos - bert_kangaroos

    # Calculate the number of days required for Bert to catch up
    days = kangaroo_difference / kangaroo_purchase_rate

    result = days
    return result

print(solution())
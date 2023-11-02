def solution():
    """Kameron has 100 kangaroos on his large farm; Bert has 20 kangaroos on his farm. In how many more days will Bert have the same number of kangaroos as Kameron does now if he buys kangaroos at the same rate of 2 new kangaroos per day?"""
    # Define initial number of kangaroos
    kam_kangaroos = 100
    bert_kangaroos = 20

    # Define rate of new kangaroos
    new_kangaroos_per_day = 2

    # Calculate the difference in kangaroos between Kameron and Bert
    kangaroo_difference = kam_kangaroos - bert_kangaroos

    # Calculate the number of days it will take for Bert to catch up
    days_to_catch_up = kangaroo_difference / new_kangaroos_per_day

    # Display the number of days it will take
    result = days_to_catch_up
    return result

print(solution())
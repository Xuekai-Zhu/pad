def solution():
    """Mark went to a store where he spent one-half of his money, and then spent $14 more. He then went to another store where he spent one-third of his starting money, and then spent $16 more. If he then had no money left, how much did he have when he entered the first store?"""
    spent_in_first_store = 14
    spent_in_second_store = 16
    fraction_remaining_after_first_store = 1/2
    fraction_remaining_after_second_store = 2/3
    total_spent = spent_in_first_store + spent_in_second_store
    remaining_fraction = 1 - total_spent/x
    x = remaining_fraction / fraction_remaining_after_second_store
    result = x
    return result

print(solution())
def solution():
    total_bottles = 35  # There are 35 bottles of milk on the grocery store shelf
    jason_buys = 5  # Jason buys 5 bottles of milk
    harry_buys = 6  # Harry buys 6 more bottles of milk

    # Calculate the remaining bottles of milk on the store shelf
    remaining_bottles = total_bottles - (jason_buys + harry_buys)
    result = remaining_bottles
    return result

print(solution())
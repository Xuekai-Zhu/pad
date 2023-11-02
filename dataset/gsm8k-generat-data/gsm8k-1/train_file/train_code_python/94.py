def solution():
    """Alice has 20 quarters. She wants to exchange them for nickels and so she goes to the bank. After getting back from the bank, she discovers that 20% of the nickels are iron nickels worth $3 each. What is the total value of her money now?"""
    quarters = 20
    nickels = quarters * 5
    iron_nickels = int(nickels * 0.2)
    regular_nickels = nickels - iron_nickels
    total_value = (regular_nickels * 0.05) + (iron_nickels * 3.00) + (quarters * 0.25)
    result = total_value
    return result

print(solution())
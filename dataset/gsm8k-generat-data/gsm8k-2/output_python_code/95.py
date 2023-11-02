def solution():
    """Alice has 20 quarters. She wants to exchange them for nickels and so she goes to the bank. After getting back from the bank, she discovers that 20% of the nickels are iron nickels worth $3 each. What is the total value of her money now?"""
    quarters = 20
    nickel_value = 0.05
    iron_nickel_percentage = 0.2
    iron_nickel_value = 3
    nickels = quarters * 5
    iron_nickels = int(nickels * iron_nickel_percentage)
    regular_nickels = nickels - iron_nickels
    total_value = regular_nickels * nickel_value + iron_nickels * iron_nickel_value
    result = total_value
    return result

print(solution())
def solution():
     """Alice has 20 quarters. She wants to exchange them for nickels and so she goes to the bank. After getting back from the bank, she discovers that 20% of the nickels are iron nickels worth $3 each. What is the total value of her money now?"""
     quarters = 20
     quarters_to_nickels = quarters * 4
     iron_nickels = quarters_to_nickels * 0.2
     regular_nickels = quarters_to_nickels - iron_nickels
     iron_nickel_value = iron_nickels * 3
     total_value = regular_nickels + iron_nickel_value
     result = total_value
     return result

print(solution())
def solution():
     """Mr. Grey is purchasing gifts for his family. So far he has purchased 3 polo shirts for $26 each; 2 necklaces for $83 each; and 1 computer game for $90. Since Mr. Grey purchased all those using his credit card, he received a $12 rebate. What is the total cost of the gifts after the rebate?"""
     polo_shirts = 3 * 26
     necklaces = 2 * 83
     computer_game = 1 * 90
     total_cost = polo_shirts + necklaces + computer_game
     rebate = 12
     total_cost_after_rebate = total_cost - rebate
     result = total_cost_after_rebate
     return result

print(solution())
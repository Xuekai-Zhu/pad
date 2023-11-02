def solution():
     """John orders food for a massive restaurant. He orders 1000 pounds of beef for $8 per pound. He also orders twice that much chicken at $3 per pound. How much did everything cost?"""
     beef_ordered = 1000
     chicken_ordered = beef_ordered * 2
     beef_cost = beef_ordered * 8
     chicken_cost = chicken_ordered * 3
     total_cost = beef_cost + chicken_cost
     
     return total_cost

print(solution())
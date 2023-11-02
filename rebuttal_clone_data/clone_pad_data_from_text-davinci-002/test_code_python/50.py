def solution():
     """Gerald spends $100 a month on baseball supplies. His season is 4 months long. He wants to use the months he's not playing baseball to save up by raking, shoveling, and mowing lawns. He charges $10 for each. How many chores does he need to average a month to save up for his supplies?"""
     monthly_cost = 100
     monthly_savings = monthly_cost / 10
     total_savings = monthly_savings * 4
     result = total_savings / 3
     return result

print(solution())
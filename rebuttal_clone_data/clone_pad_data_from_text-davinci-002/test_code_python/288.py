def solution():
     """John decides to get gym memberships so he can get in shape. The gym close to his house is close but doesn't have everything he wants so he gets two different gym memberships. The cheap one costs $10 a month and has a sign-up fee of $50. The second gym is 3 times more expensive and it has a sign-up fee of 4 months membership. How much total did he pay in the first year for gym membership?"""
     cheap_monthly_cost = 10
     expensive_monthly_cost = 3 * cheap_monthly_cost
     cheap_sign_up_fee = 50
     expensive_sign_up_fee = 4 * expensive_monthly_cost
     total_cheap_yearly_cost = cheap_sign_up_fee + (12 * cheap_monthly_cost)
     total_expensive_yearly_cost = expensive_sign_up_fee + (12 * expensive_monthly_cost)
     total_first_year_cost = total_cheap_yearly_cost + total_expensive_yearly_cost
     result = total_first_year_cost

print(solution())
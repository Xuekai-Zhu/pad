def solution():
     salary_1 = 42000
     salary_2 = 45000
     training_cost = 1200
     months_of_training = 3
     training_cost_total = training_cost * months_of_training
     first_year_earnings_1 = 93000
     first_year_earnings_2 = 92000
     percent_bonus = 1
     bonus = first_year_earnings_2 * (percent_bonus / 100)
     first_year_earnings_2_total = first_year_earnings_2 + bonus
     total_cost = training_cost_total + salary_1
     total_earnings = first_year_earnings_1 - total_cost
     total_cost_2 = salary_2 + bonus
     total_earnings_2 = first_year_earnings_2_total - total_cost_2
     result = total_earnings_2 - total_earnings
     return result

print(solution())
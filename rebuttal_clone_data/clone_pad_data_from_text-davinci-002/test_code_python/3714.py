def solution():
     job_earnings = 20 * 10
     cookie_earnings = 24 * 4
     lottery_earnings = 500
     sister_earnings = 500 * 2
     total_earnings = job_earnings + cookie_earnings + lottery_earnings + sister_earnings
     desired_amount = 5000
     amount_needed = desired_amount - total_earnings
     result = amount_needed
     
     return result

print(solution())
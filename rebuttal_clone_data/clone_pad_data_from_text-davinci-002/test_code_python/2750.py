def solution():
     total_earnings = 8000
     earnings_from_zachary = 600
     babysat_chloe = total_earnings / 5
     babysat_julie = babysat_chloe * 3
     babysat_zachary = total_earnings - (babysat_julie + babysat_chloe + earnings_from_zachary)
     result = babysat_zachary
     return result

print(solution())
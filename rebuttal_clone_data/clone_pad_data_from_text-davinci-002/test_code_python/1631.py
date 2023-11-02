def solution():
     age_difference = 2
     johns_age = 10
     when_john_is_50 = 50
     sister_age_when_john_is_50 = when_john_is_50 + (when_john_is_50 - johns_age) * age_difference
     result = sister_age_when_john_is_50
     return result

print(solution())
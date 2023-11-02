def solution():
     adult_female_alligators = 15
     total_female_alligators = adult_female_alligators / 0.4
     total_alligators = total_female_alligators / 0.5
     male_alligators = total_alligators - total_female_alligators
     result = male_alligators
     
     return result

print(solution())
def solution():
     miles_driven_per_month = 1000
     miles_driven_per_year = miles_driven_per_month * 12
     miles_between_oil_changes = 3000
     number_of_oil_changes_per_year = miles_driven_per_year / miles_between_oil_changes
     cost_of_oil_changes = number_of_oil_changes_per_year * 50
     result = cost_of_oil_changes
     return result

print(solution())
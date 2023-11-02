def solution():
     Tylenol_dosage = 1000
     time_between_doses = 6
     number_of_doses = 2
     total_number_of_pills = Tylenol_dosage / 500 * number_of_doses * time_between_doses
     result = total_number_of_pills
     return result

print(solution())
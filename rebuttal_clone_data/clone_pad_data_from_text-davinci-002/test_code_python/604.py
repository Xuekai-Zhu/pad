def solution():
     num_brothers = 7
     num_birthdays_first_half = 4
     num_birthdays_second_half = 3
     num_presents_first_half = num_birthdays_first_half * 2
     num_presents_second_half = num_birthdays_second_half * 2
     difference = num_presents_second_half - num_presents_first_half
     result = difference
     return result

print(solution())
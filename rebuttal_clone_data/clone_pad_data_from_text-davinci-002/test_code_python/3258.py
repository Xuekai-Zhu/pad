def solution():
     total_sausages = 600
     sausages_eaten_on_monday = total_sausages * (2/5)
     sausages_left = total_sausages - sausages_eaten_on_monday
     sausages_eaten_on_tuesday = sausages_left * (1/2)
     sausages_left = sausages_left - sausages_eaten_on_tuesday
     sausages_eaten_on_friday = sausages_left * (3/4)
     sausages_left = sausages_left - sausages_eaten_on_friday
     result = sausages_left
     return result

print(solution())
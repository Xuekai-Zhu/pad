def solution():
     original_length = 20
     percent_decrease = 30
     decrease_amount = original_length * (percent_decrease / 100)
     new_length = original_length - decrease_amount
     result = new_length
     return result

print(solution())
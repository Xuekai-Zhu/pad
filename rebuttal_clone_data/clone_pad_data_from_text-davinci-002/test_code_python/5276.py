def solution():
     original_num_girls = 20 * 0.40
     original_num_boys = 20 * 0.60
     new_num_boys = original_num_boys + 5
     new_num_girls = original_num_girls
     new_percent_girls = (new_num_girls / (new_num_girls + new_num_boys)) * 100
     result = new_percent_girls
     
     return result

print(solution())
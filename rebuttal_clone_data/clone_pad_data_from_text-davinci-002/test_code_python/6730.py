def solution():
     total_carrots = 300
     carrots_used_before_lunch = (2/5) * total_carrots
     carrots_left_after_lunch = total_carrots - carrots_used_before_lunch
     carrots_used_after_lunch = (3/5) * carrots_left_after_lunch
     carrots_not_used = carrots_left_after_lunch - carrots_used_after_lunch
     result = carrots_not_used
     return result

print(solution())
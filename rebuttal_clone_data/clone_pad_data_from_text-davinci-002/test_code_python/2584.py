def solution():
     total_flyers = 200
     flyers_passed_out = 42 + 67 + 51
     flyers_left = total_flyers - flyers_passed_out
     flyer_percentage = (flyers_left / total_flyers) * 100
     result = flyer_percentage
     return result

print(solution())
def solution():
     tv1_screen_size = 4800
     tv2_screen_size = 4200
     weight_per_square_inch = 4
     tv1_weight_oz = tv1_screen_size * weight_per_square_inch
     tv2_weight_oz = tv2_screen_size * weight_per_square_inch
     tv1_weight_lbs = tv1_weight_oz / 16
     tv2_weight_lbs = tv2_weight_oz / 16
     weight_difference = tv1_weight_lbs - tv2_weight_lbs
     result = weight_difference
     return result

print(solution())
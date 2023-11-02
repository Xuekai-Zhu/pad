def solution():
     stripes_on_flag = 13
     johns_flags = 10
     first_stripe = 1 #red
     remaining_stripes = stripes_on_flag - first_stripe
     number_of_red_stripes = first_stripe + (remaining_stripes / 2)
     total_red_stripes = number_of_red_stripes * johns_flags
     result = total_red_stripes
     return result

print(solution())
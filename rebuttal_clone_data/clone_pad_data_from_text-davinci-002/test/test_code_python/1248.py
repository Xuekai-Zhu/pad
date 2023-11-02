def solution():
     total_men = 80
     men_tripped = total_men / 4
     men_remaining = total_men - men_tripped
     men_dehydrated = men_remaining * (2/3)
     men_unable_to_finish = men_dehydrated * (1/5)
     men_finished = total_men - (men_tripped + men_unable_to_finish)
     result = men_finished
     return result

print(solution())
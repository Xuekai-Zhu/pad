def solution():
     shoes_1 = 40
     shoes_2 = 60
     half_off_shoes_2 = shoes_2 / 2
     total_price = shoes_1 + half_off_shoes_2
     fourth_off_total = total_price * 0.25
     final_price = total_price - fourth_off_total
     result = final_price
     return result

print(solution())
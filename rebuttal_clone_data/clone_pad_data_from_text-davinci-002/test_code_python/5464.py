def solution():
     total_milk = 16
     butter_milk = total_milk / 4
     sour_cream_milk = total_milk / 4
     whole_milk = total_milk - butter_milk - sour_cream_milk
     butter_price = 5
     sour_cream_price = 6
     whole_milk_price = 3
     total_butter_price = butter_milk * butter_price
     total_sour_cream_price = sour_cream_milk * sour_cream_price
     total_whole_milk_price = whole_milk * whole_milk_price
     total_price = total_butter_price + total_sour_cream_price + total_whole_milk_price
     result = total_price
     
     return result

print(solution())
def solution():
     salads = 2
     beef = 2
     potatoes = 1
     juice = 2
     
     salad_price = 3
     beef_price = salad_price * 2
     potatoes_price = salad_price / 3
     juice_price = 1.5
     
     total_price = (salads * salad_price) + (beef * beef_price) + (potatoes * potatoes_price) + (juice * juice_price)
     result = total_price
     return result

print(solution())
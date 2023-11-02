def solution():
     carton_of_milk = 4.00
     half_off_milk = carton_of_milk / 2
     loaf_of_bread = 3.50
     box_of_detergent = 10.25
     coupon_amount = 1.25
     detergent_after_coupon = box_of_detergent - coupon_amount
     pounds_of_bananas = 2.00
     price_per_pound = 0.75
     total_banana_price = pounds_of_bananas * price_per_pound
     total_grocery_bill = half_off_milk + loaf_of_bread + detergent_after_coupon + total_banana_price
     initial_money = 20.00
     money_left_over = initial_money - total_grocery_bill
     result = money_left_over
 
     return result

print(solution())
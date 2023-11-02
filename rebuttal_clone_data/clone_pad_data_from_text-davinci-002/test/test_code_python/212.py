def solution():
     shoes_original_price = 50
     dress_original_price = 100
     shoes_sale_discount = 40
     dress_sale_discount = 20
     shoes_sale_price = shoes_original_price - (shoes_original_price * (shoes_sale_discount / 100))
     dress_sale_price = dress_original_price - (dress_original_price * (dress_sale_discount / 100))
     total_spent = (shoes_sale_price * 2) + dress_sale_price
     result = total_spent
     return result

print(solution())
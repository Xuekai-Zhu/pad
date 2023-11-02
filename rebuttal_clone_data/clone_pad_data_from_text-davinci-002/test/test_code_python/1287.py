def solution():
     book_1_cost = 13.00
     book_2_cost = 15.00
     book_3_cost = 10.00
     book_4_cost = 10.00
     total_cost = book_1_cost + book_2_cost + book_3_cost + book_4_cost
     discount_amount = (book_1_cost + book_2_cost) * 0.25
     final_cost = total_cost - discount_amount
     shipping_cost = 50.00
     needed_to_spend = shipping_cost - final_cost
     result = needed_to_spend
     return result

print(solution())
def solution():
     total_paid = 120
     items_returned = 3
     refund_percent = 25
     refund_amount = total_paid * (refund_percent / 100)
     final_total = total_paid - refund_amount
     final_item_count = 2
     item_price = final_total / final_item_count
     result = item_price
     return result

print(solution())
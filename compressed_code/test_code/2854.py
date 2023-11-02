def solution():
    
    total_amount = 100
    five_bill_amount = 4 * 5
    twenty_bill_amount = 3 * 20
    remaining_amount = total_amount - five_bill_amount - twenty_bill_amount
    ten_bill_count = remaining_amount / 10
    result = ten_bill_count
    return result

print(solution())
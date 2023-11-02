def solution():
    
    total_amount = 120
    ten_bill_count = 0
    twenty_bill_count = 0

    
    while (twenty_bill_count * 20) <= total_amount:
        ten_bill_count = 2 * twenty_bill_count
        if (ten_bill_count * 10) + (twenty_bill_count * 20) == total_amount:
            result = twenty_bill_count
            return result
        twenty_bill_count += 1

    
    return None

print(solution())
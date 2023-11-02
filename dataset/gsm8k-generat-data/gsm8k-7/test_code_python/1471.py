def solution():
    total_amount = 120
    num_ten_bills = 0
    num_twenty_bills = 0

    # find the total number of $10 and $20 bills
    for i in range(total_amount // 10, 0, -1):
        if (total_amount - i * 10) % 20 == 0:
            num_ten_bills = i
            num_twenty_bills = (total_amount - i * 10) // 20
            break

    result = num_twenty_bills
    return result

print(solution())
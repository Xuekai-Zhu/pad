def solution():
    mandy_bills = 3
    manny_bills = 2
    mandy_to_ten = mandy_bills * 10
    manny_to_ten = manny_bills * 5
    total_bills = mandy_to_ten + manny_to_ten
    mandy_ten_bills = total_bills / 2
    manny_ten_bills = total_bills - mandy_ten_bills
    manny_extra = manny_ten_bills - mandy_ten_bills
    result = manny_extra
    return result

print(solution())
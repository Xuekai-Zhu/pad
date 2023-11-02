def solution():
     checking_account = 800
     rent = 450
     paycheck = 1500
     electricity_bill = 117
     internet_bill = 100
     phone_bill = 70
     total_bills = rent + electricity_bill + internet_bill + phone_bill
     money_left = checking_account + paycheck - total_bills
     result = money_left
     return result

print(solution())
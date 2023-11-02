def solution():
     total_money = 48
     ryans_share = 2/3
     ryans_money = total_money * ryans_share
     leos_money = total_money - ryans_money
     debts_owed = 10 + 7
     money_after_debts = leos_money - debts_owed
     result = money_after_debts
     return result

print(solution())
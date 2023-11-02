def solution():
     check_amount = 200
     tip_percentage = 20
     friend_contribution = 10
     tip_amount = check_amount * (tip_percentage / 100)
     total_amount = tip_amount + friend_contribution + check_amount
     result = total_amount
     
     return result

print(solution())
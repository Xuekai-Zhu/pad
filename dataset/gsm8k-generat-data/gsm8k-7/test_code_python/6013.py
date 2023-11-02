def solution():
    current_tip_percent = 15
    current_tip_amount = 42
    total_bill = current_tip_amount / (current_tip_percent / 100)
    
    desired_tip_percent = 20
    desired_tip_amount = total_bill * (desired_tip_percent / 100)
    result = desired_tip_amount
    return result

print(solution())
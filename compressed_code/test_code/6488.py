def solution():
    
    friend_payment = 5
    brother_payment = 8
    cousin_payment = 4
    num_days = 7
    friend_total = friend_payment * num_days
    brother_total = brother_payment * num_days
    cousin_total = cousin_payment * num_days
    total_collected = friend_total + brother_total + cousin_total
    result = total_collected
    return result

print(solution())
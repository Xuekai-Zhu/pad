def solution():
# total capacity
    capacity = 2000
# total people in stadium
    people = capacity * 3/4
# each person paid
    fee = 20
# total fees collected when 3/4 full
    total_fees1 = people * fee
# if the stadium would have been full
    total_fees2 = capacity * fee
# difference in fees
    difference = total_fees2 - total_fees1
    result = difference
    return result

print(solution())
def solution():
    
    
    total_bill = 10 + 20 + 30
    tip_percent = 20
    tip_amount = total_bill * (tip_percent/100)
    total_with_tip = total_bill + tip_amount
    num_people = 3
    tip_per_person = tip_amount/num_people
    result = tip_per_person
    return result

print(solution())
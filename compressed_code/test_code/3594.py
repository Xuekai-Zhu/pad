def solution():
    
    total_bill = 10 + 20 + 30  
    tip_percent = 0.2
    tip_amount = total_bill * tip_percent
    total_with_tip = total_bill + tip_amount
    number_of_people = 3  
    per_person_cost = total_with_tip / number_of_people
    tip_per_person = tip_amount / number_of_people

    result = tip_per_person
    return result

print(solution())
def solution():
    
    num_people = 10
    chips_per_person = 1.2
    price_per_pound = 0.25
    total_pounds = num_people * chips_per_person
    total_price = total_pounds * price_per_pound
    result = total_price
    return result

print(solution())
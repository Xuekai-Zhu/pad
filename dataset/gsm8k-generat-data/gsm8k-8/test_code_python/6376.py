def solution():
    # Find out how much each person paid when 400 people attended
    per_person_payment = 2000 / (400/2)

    # Calculate how much money they would make if 300 people attended
    new_total_payment = per_person_payment * (300/2)

    result = new_total_payment
    return result

print(solution())
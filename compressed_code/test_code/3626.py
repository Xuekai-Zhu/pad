def solution():
    
    first_showing = 200
    second_showing = 3 * first_showing
    ticket_price = 25

    first_showing_income = first_showing * ticket_price
    second_showing_income = second_showing * ticket_price

    total_income = first_showing_income + second_showing_income
    result = total_income
    return result

print(solution())
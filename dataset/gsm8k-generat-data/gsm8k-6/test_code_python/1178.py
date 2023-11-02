def solution():
    # Calculate the number of deliveries made by Tona
    deliveries_Tona = (3/4) * 96

    # Calculate the total pay earned by Oula and Tona
    pay_Oula = 96 * 100
    pay_Tona = deliveries_Tona * 100

    # Calculate their difference in pay
    diff_pay = pay_Oula - pay_Tona
    result = diff_pay
    return result

print(solution())
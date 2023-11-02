def solution():
    # Calculate the total amount Jerry is asking for
    salary_damages = 50000 * 30  # $50,000 annual salary for 30 years
    medical_bills = 200000
    punitive_damages = 3 * (salary_damages + medical_bills)
    total_damages = salary_damages + medical_bills + punitive_damages

    # Calculate the amount Jerry will receive if he gets 80% of what he's asking for
    amount_received = total_damages * 0.8
    result = amount_received
    return result

print(solution())
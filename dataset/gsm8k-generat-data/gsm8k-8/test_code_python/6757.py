def solution():
    # Define the total requested damages
    salary_damages = 50_000 * 30
    medical_damages = 200_000
    punitive_damages = 3 * (salary_damages + medical_damages)
    total_damages = salary_damages + medical_damages + punitive_damages

    # Calculate the amount Jerry will receive at 80% of his requested damages
    amount_received = total_damages * 0.8
    result = amount_received
    return result

print(solution())
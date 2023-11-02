def solution():
    """Jerry files a lawsuit against the convenience store where he works and slipped and fell. He's asking for damages for loss of a $50,000 annual salary for 30 years, $200,000 in medical bills, and punitive damages equal to triple the medical and salary damages. If he gets 80% of what he's asking for, for much money does he get?"""
    # Calculate the total damages Jerry is asking for
    salary_damages = 50000 * 30
    medical_damages = 200000
    punitive_damages = 3 * (salary_damages + medical_damages)
    total_damages = salary_damages + medical_damages + punitive_damages

    # Calculate the amount Jerry actually receives if he gets 80% of what he's asking for
    final_amount = total_damages * 0.8

    # Display the final amount Jerry receives
    result = final_amount
    return result

print(solution())
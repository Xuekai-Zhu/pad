def solution():
    """Jerry files a lawsuit against the convenience store where he works and slipped and fell. He's asking for damages for loss of a $50,000 annual salary for 30 years, $200,000 in medical bills, and punitive damages equal to triple the medical and salary damages. If he gets 80% of what he's asking for, for much money does he get?"""
    # Define the damages being sought by Jerry
    salary_damages = 50000 * 30
    medical_damages = 200000
    punitive_damages = (salary_damages + medical_damages) * 3

    # Calculate the total damages being sought by Jerry
    total_damages = salary_damages + medical_damages + punitive_damages

    # Calculate the amount Jerry receives if he gets 80% of what he's asking for
    amount_received = total_damages * 0.8

    result = amount_received
    return result

print(solution())
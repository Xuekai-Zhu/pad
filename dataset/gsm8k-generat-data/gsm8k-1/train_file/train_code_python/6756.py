def solution():
    """Jerry files a lawsuit against the convenience store where he works and slipped and fell. He's asking for damages for loss of a $50,000 annual salary for 30 years, $200,000 in medical bills, and punitive damages equal to triple the medical and salary damages. If he gets 80% of what he's asking for, for much money does he get?"""
    salary_loss = 50000 * 30
    medical_bills = 200000
    punitive_damages = 3 * (salary_loss + medical_bills)
    total_requested = salary_loss + medical_bills + punitive_damages
    amount_received = total_requested * 0.8
    result = amount_received
    return result

print(solution())
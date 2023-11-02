def solution():
    """James takes 2 Tylenol tablets that are 375 mg each, every 6 hours. How many mg does he take a day?"""
    # Define the Tylenol dose and frequency
    tylenol_dose = 375 * 2
    tylenol_frequency = 24 / 6  # 4 times a day

    # Calculate the total daily dose of Tylenol
    total_dose = tylenol_dose * tylenol_frequency

    result = total_dose
    return result

print(solution())
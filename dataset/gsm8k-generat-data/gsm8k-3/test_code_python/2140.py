def solution():
    """James takes 2 Tylenol tablets that are 375 mg each, every 6 hours.  How many mg does he take a day?"""
    # Define the dosage of each tablet and the frequency of intake
    DOSE = 375 * 2
    FREQUENCY = 4  # 24 hours divided by 6 hours per dosage

    # Calculate the total dosage per day
    total_dosage = DOSE * FREQUENCY

    # Display the total dosage per day
    result = total_dosage
    return result

print(solution())
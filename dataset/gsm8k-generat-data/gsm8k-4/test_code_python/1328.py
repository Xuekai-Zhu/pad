def solution():
    """Daniel owns a textile company. Every Monday he delivers 20 yards of fabric, and every Tuesday he delivers twice the amount of fabric he delivers on Monday. Every Wednesday, he delivers 1/4 of the amount of fabric he delivers on Tuesday. If each yard of fabric costs $2 and each yard of yarn costs $3, how much does he earn from Monday to Wednesday?"""
    # Define the amount of fabric delivered on Monday and calculate the earnings
    fabric_monday = 20
    earnings_monday = fabric_monday * 2

    # Define the amount of fabric delivered on Tuesday and calculate the earnings
    fabric_tuesday = 2 * fabric_monday
    earnings_tuesday = fabric_tuesday * 2

    # Define the amount of fabric delivered on Wednesday and calculate the earnings
    fabric_wednesday = fabric_tuesday / 4
    earnings_wednesday = fabric_wednesday * 2

    # Calculate the total earnings from Monday to Wednesday
    total_earnings = (earnings_monday + earnings_tuesday + earnings_wednesday) * 2

    # Display the result
    result = total_earnings
    return result

print(solution())
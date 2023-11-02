def solution():
    """Valerie’s cookie recipe makes 16 dozen cookies and calls for 4 pounds of butter. She only wants to make 4 dozen cookies for the weekend. How many pounds of butter will she need?"""
    # Define the amount of cookies and butter required for the original recipe
    cookies_original = 16 * 12
    butter_original = 4

    # Calculate the proportion of cookies and butter needed for 4 dozen cookies
    cookies_needed = 4 * 12
    butter_needed = (cookies_needed / cookies_original) * butter_original

    # Round the amount of butter needed to the nearest tenth
    butter_needed = round(butter_needed, 1)

    result = butter_needed
    return result

print(solution())
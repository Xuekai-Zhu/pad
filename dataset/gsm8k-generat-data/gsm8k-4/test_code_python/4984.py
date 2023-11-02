def solution():
    """Bill and Joan both work for a library. 5 years ago, Joan had 3 times as much experience as Bill. Now she has twice as much experience as Bill. How many years of experience does Bill have now?"""
    # Define the number of years of experience Bill had 5 years ago
    bill_5_years_ago = None

    # Define the number of years of experience Joan had 5 years ago
    joan_5_years_ago = bill_5_years_ago * 3

    # Calculate the current number of years of experience for Joan and Bill
    total_years = (joan_5_years_ago + 5) + (bill_5_years_ago + 5)

    # Calculate the current number of years of experience for Bill
    bill_years = (total_years / 3) - 5

    result = bill_years
    return result

print(solution())
def solution():
    """Tim and Donna will celebrate their 20th wedding anniversary in 2025.  They started dating 3 years before they got married and met 2 years before that.  When did they meet?"""
    # Define the year of their 20th wedding anniversary
    WEDDING_ANNIVERSARY_YEAR = 2025

    # Calculate the year they got married
    marriage_year = WEDDING_ANNIVERSARY_YEAR - 20

    # Calculate the year they started dating
    dating_year = marriage_year - 3

    # Calculate the year they met
    meeting_year = dating_year - 2

    # Display the year they met
    result = meeting_year
    return result

print(solution())
def solution():
    """Tim and Donna will celebrate their 20th wedding anniversary in 2025. They started dating 3 years before they got married and met 2 years before that. When did they meet?"""
    wedding_year = 2025
    dating_years = 3
    meeting_years = 2
    years_since_meeting = wedding_year - dating_years - meeting_years - 20
    meeting_year = wedding_year - years_since_meeting
    result = meeting_year
    return result

print(solution())
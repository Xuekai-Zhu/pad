def solution():
    members = 100  # There are 100 church members baking cookies
    sheets_per_member = 10  # Each member bakes 10 sheets of cookies
    cookies_per_sheet = 16  # Each sheet has 16 cookies

    # Calculate the total number of cookies baked by the church members
    total_cookies = members * sheets_per_member * cookies_per_sheet
    result = total_cookies
    return result

print(solution())
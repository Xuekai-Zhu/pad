def solution():
    #Define the number of members and sheets baked by each member
    num_members = 100
    sheets_per_member = 10

    #Calculate the total number of sheets baked
    total_sheets = num_members * sheets_per_member

    #Calculate the total number of cookies baked
    cookies_per_sheet = 16
    total_cookies = total_sheets * cookies_per_sheet

    result = total_cookies
    return result

print(solution())
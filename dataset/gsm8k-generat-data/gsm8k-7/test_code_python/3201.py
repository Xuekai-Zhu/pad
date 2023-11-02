def solution():
    num_members = 100
    num_sheets_per_member = 10
    num_cookies_per_sheet = 16
    
    # Calculate the total number of sheets of cookies baked by all members
    total_sheets = num_members * num_sheets_per_member
    
    # Calculate the total number of cookies baked by all members
    total_cookies = total_sheets * num_cookies_per_sheet
    result = total_cookies
    return result

print(solution())
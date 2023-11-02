def solution():
    """A church has 100 members who've volunteered to bake cookies for the homeless in their local town. If each member baked 10 sheets of cookies, and each sheet has 16 cookies, calculate the total number of cookies the church members baked?"""
    
    # Define the number of members and amount of cookies per member
    members = 100
    sheets_per_member = 10
    cookies_per_sheet = 16
    
    # Calculate the total number of cookies baked
    total_cookies = members * sheets_per_member * cookies_per_sheet
    
    # Display the total number of cookies
    result = total_cookies
    return result

print(solution())
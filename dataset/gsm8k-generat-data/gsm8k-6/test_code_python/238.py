def solution():
    # Calculate the total amount Jack has already made
    total_made = 4*3 + 5*2  # Jack sold 4 brownies for $3 and 5 lemon squares for $2 each

    # Calculate the amount Jack needs to make with cookies to reach his goal
    needed_amount = 50 - total_made

    # Calculate the number of cookies Jack needs to sell to make the needed amount
    num_cookies = needed_amount / 4  # Jack sells cookies for $4 each

    result = num_cookies
    return result

print(solution())
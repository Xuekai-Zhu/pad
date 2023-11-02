def solution():
    # Calculate the total number of cookies
    total_cookies = 3*12 + 2*12 + 4*12  # three dozen oatmeal raisin cookies, two dozen sugar cookies, and four dozen chocolate chip cookies
    given_away_cookies = 2*12 + 1.5*12 + 2.5*12  # two dozen oatmeal raisin cookies, 1.5 dozen sugar cookies, and 2.5 dozen chocolate chip cookies given away
    remaining_cookies = total_cookies - given_away_cookies  # total number of cookies Ann kept

    result = remaining_cookies
    return result

print(solution())
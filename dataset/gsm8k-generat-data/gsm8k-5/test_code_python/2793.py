def solution():
    trays = 4  # Lara is using 4 baking trays
    rows_per_tray = 5  # Lara places 5 rows of cookies on each tray
    cookies_per_row = 6  # Each row has 6 cookies

    # Calculate the total number of cookies Lara is baking
    total_cookies = trays * rows_per_tray * cookies_per_row
    result = total_cookies
    return result

print(solution())
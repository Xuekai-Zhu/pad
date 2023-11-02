def solution():
    """Lara is baking cookies using four baking trays. She places five rows of cookies on a baking tray where there are six cookies in one row. How many cookies is she baking?"""
    
    # Define the number of baking trays and rows of cookies per tray
    num_trays = 4
    num_rows = 5
    num_cookies_per_row = 6

    # Calculate the total number of cookies
    total_cookies = num_trays * num_rows * num_cookies_per_row

    # Display the total number of cookies
    result = total_cookies
    return result

print(solution())
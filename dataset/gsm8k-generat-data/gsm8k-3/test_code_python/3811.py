def solution():
    """Carmen is selling girl scout cookies. She sells three boxes of samoas to the green house for $4 each; two boxes of thin mints for $3.50 each and one box of fudge delights for $5 to the yellow house; and nine boxes of sugar cookies for $2 each to the brown house. How much money did Carmen make?"""
    # Define the prices of each type of cookie
    SAMOA_PRICE = 4
    THIN_MINT_PRICE = 3.5
    FUDGE_DELIGHT_PRICE = 5
    SUGAR_COOKIE_PRICE = 2

    # Define the number of boxes sold to each house
    green_boxes = 3
    yellow_boxes = 1
    brown_boxes = 9

    # Calculate the total sales for each type of cookie
    samoa_sales = green_boxes * SAMOA_PRICE
    thin_mint_sales = 2 * THIN_MINT_PRICE
    fudge_delight_sales = yellow_boxes * FUDGE_DELIGHT_PRICE
    sugar_cookie_sales = brown_boxes * SUGAR_COOKIE_PRICE

    # Calculate the total sales for all cookies
    total_sales = samoa_sales + thin_mint_sales + fudge_delight_sales + sugar_cookie_sales

    # Display the total sales
    result = total_sales
    return result

print(solution())
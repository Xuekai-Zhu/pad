def solution():
    """Haley is making cider. It takes 20 golden delicious apples and 40 pink lady apples to make one pint of cider. Each of her 6 farmhands can pick 240 apples per hour and will work 5 hours today. How many pints of cider can Haley make with the apples gathered today, provided that the ratio of golden delicious apples to pink lady apples gathered is 1:2?"""
    # Define the number of apples needed to make one pint of cider
    GOLDEN_APPLES_PER_PINT = 20
    PINK_APPLES_PER_PINT = 40

    # Define the ratio of golden delicious apples to pink lady apples gathered
    GOLDEN_TO_PINK_RATIO = 1/2

    # Calculate the number of golden delicious apples and pink lady apples gathered
    total_apples_gathered = 6 * 240 * 5
    golden_apples_gathered = total_apples_gathered / 3
    pink_apples_gathered = total_apples_gathered * 2 / 3

    # Calculate the number of pints of cider that can be made
    pints_of_cider = min(golden_apples_gathered // GOLDEN_APPLES_PER_PINT, pink_apples_gathered // PINK_APPLES_PER_PINT)

    # Display the number of pints of cider that can be made
    result = pints_of_cider
    return result

print(solution())
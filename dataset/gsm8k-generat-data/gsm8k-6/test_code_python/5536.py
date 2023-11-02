def solution():
    total_earnings = 380  # total earnings
    broccoli_sales = 57  # sales from broccoli
    carrot_sales = 2 * broccoli_sales  # sales from carrots is twice as much as broccoli
    spinach_sales = (1/2 * carrot_sales) + 16  # sales from spinach is $16 more than half of the sales of carrots
    cauliflower_sales = total_earnings - (broccoli_sales + carrot_sales + spinach_sales)  # earnings from cauliflower sales is the difference between total earnings and other sales
    result = cauliflower_sales
    return result

print(solution())
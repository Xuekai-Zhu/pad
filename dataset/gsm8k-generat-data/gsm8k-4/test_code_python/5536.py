def solution():
    """Maya's organization hosted a weekly farmers' market to raise money for the church choir. They sold broccolis, carrots, spinach, and cauliflowers. After adding together all of their earnings, Maya found out that they had made $380. The organization made $57 from broccoli and the sales of the carrots are twice as much as the sales of broccoli. Then, their sales for the spinach is $16 more than half of the sales of carrots. How much did they make from cauliflower sales?"""
    # Define the total earnings and earnings from broccoli sales
    total_earnings = 380
    broccoli_earnings = 57

    # Calculate the earnings from carrot sales
    carrot_earnings = broccoli_earnings * 2

    # Calculate the sales of carrots
    carrot_sales = carrot_earnings / 0.5

    # Calculate the sales of spinach
    spinach_sales = (carrot_sales / 2 + 16) / 0.4

    # Calculate the earnings from cauliflower sales
    cauliflower_earnings = total_earnings - broccoli_earnings - carrot_earnings - spinach_sales * 0.4

    # Return the result
    result = cauliflower_earnings
    return result

print(solution())
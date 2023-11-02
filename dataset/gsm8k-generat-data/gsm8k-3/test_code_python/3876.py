def solution():
    """On Thursday the Meat Market sold 210kg of ground beef. On Friday they sold twice that amount. On Saturday they only sold 130kg. On Sunday they sold half of what they sold Saturday. If they originally planned to sell only 500kg, how much meat did they sell beyond their original plans?"""
    # Calculate the amount of ground beef sold on each day
    thursday_sales = 210
    friday_sales = 2 * thursday_sales
    saturday_sales = 130
    sunday_sales = 0.5 * saturday_sales

    # Calculate the total amount of ground beef sold
    total_sales = thursday_sales + friday_sales + saturday_sales + sunday_sales

    # Calculate the amount of meat sold beyond their original plans
    beyond_plan = total_sales - 500

    # Display the amount of meat sold beyond their original plans
    result = beyond_plan
    return result

print(solution())
def solution():
    """Village Foods sells good food at a fair price.  Their specialty is fresh vegetables.  If they get 500 customers per month, and each customer purchases 2 heads of lettuce for $1 each and 4 tomatoes for $0.5 apiece, then how much money, in dollars, will the store receive in sales of lettuce and tomatoes per month?"""
    
    # Calculate the total number of lettuce heads sold
    lettuce_heads_sold = 500 * 2

    # Calculate the total revenue from lettuce sales
    lettuce_revenue = lettuce_heads_sold * 1

    # Calculate the total number of tomatoes sold
    tomatoes_sold = 500 * 4

    # Calculate the total revenue from tomato sales
    tomato_revenue = tomatoes_sold * 0.5

    # Calculate the total revenue from lettuce and tomato sales
    total_revenue = lettuce_revenue + tomato_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())
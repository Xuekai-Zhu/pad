def solution():
    """On a tough week, Haji's mother sells goods worth $800, which is half the amount she sells on a good week. What's the total amount of money she makes if she has 5 good weeks and 3 tough weeks?"""
    # Define the amount of sales on a tough week and calculate the amount on a good week
    tough_sales = 800
    good_sales = tough_sales * 2

    # Calculate the total amount of sales over the 8 weeks
    total_sales = (good_sales * 5) + (tough_sales * 3)

    # Display the total amount of sales
    result = total_sales
    return result

print(solution())
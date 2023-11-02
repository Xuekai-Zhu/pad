def solution():
    """On Friday, Hank opens his used-bicycle store with a stock of bicycles, all fixed-up and ready to ride. Over the course of the day, he sold 10 bicycles and bought an additional 15 to fix up. On Saturday, he sold 12 bicycles and bought eight more. And on Sunday, he sold nine bicycles and bought 11 more. What is the net increase in the number of bicycles in stock in Hank's store over the three days?"""
    friday_sold = 10
    friday_bought = 15
    saturday_sold = 12
    saturday_bought = 8
    sunday_sold = 9
    sunday_bought = 11
    total_sold = friday_sold + saturday_sold + sunday_sold
    total_bought = friday_bought + saturday_bought + sunday_bought
    net_increase = total_bought - total_sold
    result = net_increase
    return result

print(solution())
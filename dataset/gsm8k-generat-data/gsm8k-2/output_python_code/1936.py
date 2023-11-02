def solution():
    """On Friday, Hank opened his used-bicycle store with a stock of bicycles, all fixed-up and ready to ride. Over the course of the day, he sold 10 bicycles and bought an additional 15 to fix up. On Saturday, he sold 12 bicycles and bought 8 more. And on Sunday, he sold 9 bicycles and bought 11 more. What was the net increase in the number of bicycles in stock in Hank's store over the three days?"""
    friday_start = 0
    friday_sold = 10
    friday_fixed = 15
    friday_end = friday_start + friday_fixed - friday_sold
    saturday_start = friday_end
    saturday_sold = 12
    saturday_fixed = 8
    saturday_end = saturday_start + saturday_fixed - saturday_sold
    sunday_start = saturday_end
    sunday_sold = 9
    sunday_fixed = 11
    sunday_end = sunday_start + sunday_fixed - sunday_sold
    net_increase = sunday_end - friday_start
    result = net_increase
    return result

print(solution())
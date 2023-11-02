def solution():
    total_purchase = 3000
    tv_cost = 700
    bike_returned_cost = 500
    bike_sold_cost = bike_returned_cost * 1.2 * 0.8  # 20% more than the returned bike and sold for 80% of what he bought it for
    toaster_cost = 100

    total_refunds = tv_cost + bike_returned_cost
    total_sales = bike_sold_cost
    total_expenses = total_purchase - total_refunds + toaster_cost
    total_out_of_pocket = total_expenses - total_sales
    result = total_out_of_pocket
    return result

print(solution())
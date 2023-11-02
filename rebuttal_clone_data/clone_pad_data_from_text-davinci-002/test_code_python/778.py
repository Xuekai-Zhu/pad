def solution():
    cost_of_items = 3000
    cost_of_tv = 700
    cost_of_bike = 500
    amount_refunded_for_tv = cost_of_tv
    amount_refunded_for_bike = cost_of_bike
    cost_of_bike_sold = cost_of_bike * 1.2
    amount_received_for_bike_sold = cost_of_bike_sold * 0.8
    cost_of_toaster = 100
    total_out_of_pocket = cost_of_items - amount_refunded_for_tv - amount_refunded_for_bike + cost_of_toaster - amount_received_for_bike_sold
    result = total_out_of_pocket
    return result

print(solution())
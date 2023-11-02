def solution():
    # Calculate the cost per load of laundry
    regular_price = 25  # cost of one bottle of detergent
    sale_price = 20  # cost of one bottle during the sale
    bottles = 2  # number of bottles purchased
    loads = 80 * bottles  # total number of loads that can be washed with two bottles
    cost_regular = regular_price / loads  # cost per load using regular price
    cost_sale = sale_price / loads  # cost per load using sale price
    result = int(cost_sale * 100)  # convert to cents and return as integer
    return result

print(solution())
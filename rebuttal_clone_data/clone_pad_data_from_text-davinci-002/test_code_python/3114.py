def solution():
    customer_one = 5
    customer_two = customer_one * 4
    customer_three = customer_two / 2
    customer_four = customer_three * 3
    customer_five = 10
    total_sold = customer_one + customer_two + customer_three + customer_four + customer_five
    boxes_left = 150 - total_sold
    result = boxes_left
    return result

print(solution())
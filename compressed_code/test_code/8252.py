def solution():
    
    sales_goal = 150
    first_customer = 5
    second_customer = 4 * first_customer
    third_customer = second_customer / 2
    fourth_customer = 3 * third_customer
    final_customer = 10
    total_sold = first_customer + second_customer + third_customer + fourth_customer + final_customer
    boxes_left = sales_goal - total_sold
    result = boxes_left
    return result

print(solution())
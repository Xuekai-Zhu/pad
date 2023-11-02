def solution():
    
    # Define the number of CDs and the cost per CD
    num_cds = 10
    cost_per_cd = 15

    # Calculate the total cost before the discount
    total_cost_before_discount = num_cds * cost_per_cd

    # Calculate the cost after the discount
    cost_after_discount = total_cost_before_discount * 0.6

    # Calculate the cost after the discount
    cost_after_discount = total_cost_before_discount - cost_after_discount

    # Calculate the number of CDs James didn't like
    num_cds_no_like = 5

    # Calculate the number of CDs James sells
    num_cds_sold = 40

    # Calculate the total amount of money James was out
    total_money_out = cost_after_discount - num_cds_sold

    # Display the total amount of money James was out
    result = total_money_out
    return result

print(solution())
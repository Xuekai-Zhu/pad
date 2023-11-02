def solution():
    # Calculate the total amount paid for 400 peaches at 40 cents each
    total_price = 400 * 0.40 

    # Calculate the number of $10 purchases made
    num_purchases = total_price // 10  

    # Calculate the total discount received
    total_discount = num_purchases * 2  

    # Calculate the final amount paid by Kataleya
    final_amount = total_price - total_discount  
    result = final_amount
    return result

print(solution())
def solution():
    
    # Define the number of pupils and the number of coupons
    num_pupils = 29
    num_coupons = 9

    # Calculate the total number of bottles of apple juice redeemed
    total_redeemed = num_coupons * 100

    # Calculate the total number of bottles of apple juice given to lunch
    total_given = num_coupons * 2

    # Calculate the total number of bottles of apple juice
    total_apple_juice = total_redeemed + total_given

    # Display the total number of bottles of apple juice
    result = total_apple_juice
    return result

print(solution())
def solution():
    
    # Define the number of pupils and coupons
    pupils = 29
    coupons = 9

    # Calculate the total number of bottles of apple juice redeemed
    total_redeemed = coupons * 100

    # Calculate the total number of bottles of apple juice given to lunch
    total_given = total_redeemed * 2

    # Calculate the total number of bottles of apple juice the teacher has for herself
    total_juice = total_given + total_given

    # Display the total number of bottles of apple juice the teacher has for herself
    result = total_juice
    return result

print(solution())
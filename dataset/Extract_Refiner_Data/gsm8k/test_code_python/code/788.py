def solution():
    
    # Define the number of bottle caps found per day and the price per bottle cap
    BOTTLE_CAPS_PER_DAY = 10
    BOTTLE_CAP_PRICE = 0.25

    # Calculate the total number of bottle caps found in a 30 day month
    total_bottle_caps = BOTTLE_CAPS_PER_DAY * 30

    # Calculate the total amount of money Damien makes in a 30 day month
    total_money = total_bottle_caps * BOTTLE_CAP_PRICE

    # Display the total money Damien makes in a 30 day month
    result = total_money
    return result

print(solution())
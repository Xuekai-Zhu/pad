def solution():
    num_cows = 12
    milk_per_cow = 4  # in gallons
    milk_price = 3  # per gallon
    butter_price = 1.5  # per stick
    milk_to_butter_ratio = 2  # 1 gallon of milk = 2 sticks of butter
    num_customers = 6
    milk_per_customer = 6  # in gallons

    # Calculate the total amount of milk produced
    total_milk = num_cows * milk_per_cow

    # Calculate the total amount of milk sold to customers
    milk_to_sell = num_customers * milk_per_customer
    milk_leftover = total_milk - milk_to_sell  # milk that will be turned into butter
    total_milk_revenue = milk_to_sell * milk_price

    # Calculate the total amount of butter produced
    total_butter = milk_leftover / milk_to_butter_ratio

    # Calculate the total revenue from selling butter
    total_butter_revenue = total_butter * butter_price

    # Calculate the total revenue from selling milk and butter
    total_revenue = total_milk_revenue + total_butter_revenue
    result = total_revenue
    return result

print(solution())
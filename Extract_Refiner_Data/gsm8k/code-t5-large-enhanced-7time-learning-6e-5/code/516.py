def solution():
    
    # Define the number of grandchildren
    NUM_GRANDCHILDREN = 3

    # Define the number of each item needed
    hat_count = 2
    scarf_count = 4
    sweater_count = 12
    mittens_count = 1
    socks_count = 2

    # Calculate the total number of items needed
    total_items = hat_count + scarf_count + sweater_count + mittens_count + socks_count

    # Calculate the total number of skeins needed
    total_skeins = total_items * NUM_GRANDCHILDREN

    # Display the total number of skeins needed
    result = total_skeins
    return result

print(solution())
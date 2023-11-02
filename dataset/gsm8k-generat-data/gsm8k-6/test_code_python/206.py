def solution():
    # Calculate the net increase in the number of lions every month
    net_increase = 5 - 1  # 5 lion cubs are born and 1 lion dies every month

    # Calculate the total net increase in the number of lions in 12 months
    total_increase = net_increase * 12

    # Calculate the number of lions at first given the number of lions after 1 year
    lions_at_first = 148 - total_increase
    result = lions_at_first
    return result

print(solution())
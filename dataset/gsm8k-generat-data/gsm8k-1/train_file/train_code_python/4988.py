def solution():
    """Edmund owns a gift wrapping shop, he uses 18 inches of gift wrapper per gift box. If Edmund has 90 inches of gift wrapper per day, how many gift boxes will he be able to wrap every 3 days?"""
    wrapper_per_box = 18
    wrapper_per_day = 90
    days = 3
    wrapper_available = wrapper_per_day * days
    boxes_wrapped = wrapper_available // wrapper_per_box
    result = boxes_wrapped
    return result

print(solution())
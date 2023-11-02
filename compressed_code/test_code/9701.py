def solution():
    
    wrapper_per_box = 18
    wrapper_per_day = 90
    days = 3
    wrapper_available = wrapper_per_day * days
    boxes_wrapped = wrapper_available // wrapper_per_box
    result = boxes_wrapped
    return result

print(solution())
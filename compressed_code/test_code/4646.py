def solution():
    
    total_tabs = 400
    first_close = total_tabs * 0.25
    remaining_tabs = total_tabs - first_close
    second_close = remaining_tabs * 0.4
    remaining_tabs -= second_close
    third_close = remaining_tabs / 2
    remaining_tabs -= third_close
    result = remaining_tabs
    return result

print(solution())
def solution():
    
    first_box_price = 2
    first_box_count = 10
    second_box_price = 5
    second_box_count = 5
    total_cost = (first_box_price * first_box_count) + (second_box_price * second_box_count)
    total_count = first_box_count + second_box_count
    avg_price = total_cost / total_count
    result = avg_price
    return result

print(solution())
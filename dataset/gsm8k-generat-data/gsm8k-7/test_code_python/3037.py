def solution():
    total_visitors = 500
    ill_percent = 0.40  # 40% of visitors fell ill

    # Calculate the number of visitors who fell ill
    num_ill = total_visitors * ill_percent

    # Calculate the number of visitors who did not fall ill
    num_not_ill = total_visitors - num_ill
    result = num_not_ill
    return result

print(solution())
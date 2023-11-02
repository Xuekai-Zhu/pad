def solution():
    total_visitors = 500  # There were 500 visitors to the aquarium
    percent_ill = 40  # 40 percent of visitors fell ill

    # Calculate the number of visitors who did not fall ill
    visitors_not_ill = total_visitors * (1 - percent_ill/100)
    result = visitors_not_ill
    return result

print(solution())
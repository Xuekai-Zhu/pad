def solution():
    
    total_flowers = 25 + 40 + 35
    non_rose_flowers = total_flowers - 25
    percentage_non_rose = (non_rose_flowers / total_flowers) * 100
    result = percentage_non_rose
    return result

print(solution())
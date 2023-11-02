def solution():
    
    total_roses = 25
    total_tulips = 40
    total_daisies = 35
    total_flowers = total_roses + total_tulips + total_daisies
    non_rose_flowers = total_flowers - total_roses
    percentage_non_roses = (non_rose_flowers / total_flowers) * 100
    result = percentage_non_roses
    return result

print(solution())
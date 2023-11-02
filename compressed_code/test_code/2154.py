def solution():
    
    total_flowers = 52
    mom_flowers = 15
    grandma_flowers = mom_flowers + 6
    remaining_flowers = total_flowers - mom_flowers - grandma_flowers
    result = remaining_flowers
    return result

print(solution())
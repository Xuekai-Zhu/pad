def solution():
    total_flowers = 400
    tulips = 120
    roses = total_flowers - tulips
    white_roses = 80
    red_roses = roses - white_roses
    total_red_roses = red_roses * 2
    half_red_roses = total_red_roses / 2
    rose_price = 0.75
    total_earnings = half_red_roses * rose_price
    result = total_earnings
    
    return result

print(solution())
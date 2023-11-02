def solution():
    liam_oranges = 40
    liam_price = 2.50
    liam_ total = liam_oranges * liam_price
    
    claire_oranges = 30
    claire_price = 1.20
    claire_total = claire_oranges * claire_price
    
    total_oranges = liam_oranges + claire_oranges
    total_price = liam_total + claire_total
    
    answer = total_price
    return answer

print(solution())
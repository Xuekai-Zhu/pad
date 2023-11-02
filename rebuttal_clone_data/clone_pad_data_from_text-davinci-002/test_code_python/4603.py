def solution():
  
    cats = 6
    female_cats = cats / 2
    kittens = female_cats * 7
    cats_sold = 9
    remaining_cats = kittens - cats_sold
    kittens_percent = (remaining_cats / kittens) * 100
    result = kittens_percent
    
    return result

print(solution())
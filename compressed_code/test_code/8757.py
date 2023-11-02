def solution():
    
    total_bottles = 180
    cider_bottles = 40
    beer_bottles = 80
    mixed_bottles = total_bottles - cider_bottles - beer_bottles
    first_house_bottles = (cider_bottles + beer_bottles + mixed_bottles) / 2
    result = first_house_bottles
    return result

print(solution())
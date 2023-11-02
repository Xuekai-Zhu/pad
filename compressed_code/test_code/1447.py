def solution():
    
    total_animals = 300
    cats = total_animals * (2/3)  
    dogs = total_animals - cats  
    dog_legs = dogs * 4  
    result = dog_legs
    return result

print(solution())
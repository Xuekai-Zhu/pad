def solution():
    
    dogs = 5
    cats = 2
    birds = 10
    legs_per_dog = 4
    legs_per_cat = 4
    legs_per_bird = 4
    total_legs = (dogs * legs_per_dog) + (cats * legs_per_cat) + (birds * legs_per_bird)
    result = total_legs
    return result

print(solution())
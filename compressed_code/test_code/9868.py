def solution():
    
    total_vets = 1000
    puppy_kibble_percent = 20
    yummy_dog_kibble_percent = 30
    puppy_kibble_recommendations = (puppy_kibble_percent / 100) * total_vets
    yummy_dog_kibble_recommendations = (yummy_dog_kibble_percent / 100) * total_vets
    difference = yummy_dog_kibble_recommendations - puppy_kibble_recommendations
    result = difference
    return result

print(solution())
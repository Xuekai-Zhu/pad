def solution():
    """20% of the vets in a state recommend Puppy Kibble. 30% recommend Yummy Dog Kibble. If there are 1000 vets in the state, how many more recommend Yummy Dog Kibble than Puppy Kibble?"""
    total_vets = 1000
    puppy_kibble_percent = 20
    yummy_dog_kibble_percent = 30
    puppy_kibble_recommendations = (puppy_kibble_percent / 100) * total_vets
    yummy_dog_kibble_recommendations = (yummy_dog_kibble_percent / 100) * total_vets
    difference = yummy_dog_kibble_recommendations - puppy_kibble_recommendations
    result = difference
    return result

print(solution())
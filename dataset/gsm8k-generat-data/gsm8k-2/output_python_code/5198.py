def solution():
    """20% of the vets in a state recommend Puppy Kibble. 30% recommend Yummy Dog Kibble. If there are 1000 vets in the state, how many more recommend Yummy Dog Kibble than Puppy Kibble?"""
    total_vets = 1000
    puppy_kibble_vets = total_vets * 0.2
    yummy_dog_kibble_vets = total_vets * 0.3
    difference = yummy_dog_kibble_vets - puppy_kibble_vets
    result = difference
    return result

print(solution())
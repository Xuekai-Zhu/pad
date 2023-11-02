def solution():
    total_vets = 1000  # There are 1000 vets in the state
    puppy_kibble_vets = 0.20 * total_vets  # 20% of the vets recommend Puppy Kibble
    yummy_dog_kibble_vets = 0.30 * total_vets  # 30% of the vets recommend Yummy Dog Kibble

    # Calculate the difference in the number of vets recommending Yummy Dog Kibble and Puppy Kibble
    difference = yummy_dog_kibble_vets - puppy_kibble_vets
    result = difference
    return result

print(solution())
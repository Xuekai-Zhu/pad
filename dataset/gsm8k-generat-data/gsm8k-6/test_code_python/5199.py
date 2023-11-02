def solution():
    # Calculate the number of vets who recommend Puppy Kibble
    puppy_kibble_recommend = 0.20 * 1000

    # Calculate the number of vets who recommend Yummy Dog Kibble
    yummy_kibble_recommend = 0.30 * 1000

    # Calculate the difference between the number of vets who recommend Yummy Dog Kibble and Puppy Kibble
    difference = yummy_kibble_recommend - puppy_kibble_recommend
    result = difference
    return result

print(solution())
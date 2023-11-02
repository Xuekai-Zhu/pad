def solution():
    vets_in_state = 1000
    percent_recommended_puppy_kibble = 20
    percent_recommended_yummy_kibble = 30
    recommended_puppy_kibble = vets_in_state * (percent_recommended_puppy_kibble / 100)
    recommended_yummy_kibble = vets_in_state * (percent_recommended_yummy_kibble / 100)
    difference = recommended_yummy_kibble - recommended_puppy_kibble
    result = difference
    return result

print(solution())
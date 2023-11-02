def solution():
    total_candies = 300
    sour_candies = 0.4 * total_candies
    good_candies = total_candies - sour_candies
    brothers = 2
    good_candies_per_person = good_candies / brothers
    result = good_candies_per_person
    return result

print(solution())
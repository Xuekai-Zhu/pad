def solution():
    
    total_candies = 300
    sour_candies = total_candies * 0.4
    good_candies = total_candies - sour_candies
    num_people = 3
    good_candies_per_person = good_candies // num_people
    result = good_candies_per_person
    return result

print(solution())
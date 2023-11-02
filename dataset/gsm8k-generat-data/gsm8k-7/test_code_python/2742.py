def solution():
    num_candies = 300
    num_brothers = 2
    sour_percentage = 0.4

    # Calculate the number of sour candies
    num_sour_candies = num_candies * sour_percentage

    # Calculate the number of good candies
    num_good_candies = num_candies - num_sour_candies

    # Calculate the number of good candies each person gets after sharing equally
    num_candies_per_person = num_good_candies / (num_brothers + 1)

    result = num_candies_per_person
    return result

print(solution())
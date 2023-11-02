def solution():
    # Calculate the total number of candies
    total_candies = 30 + 25 + 35

    # Calculate how many candies each person will get
    candies_per_person = total_candies // 3  # the // symbol denotes integer division

    result = candies_per_person
    return result

print(solution())
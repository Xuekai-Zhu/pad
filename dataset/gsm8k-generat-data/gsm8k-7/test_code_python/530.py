def solution():
    num_cookies = 42
    num_candy = 63
    num_brownies = 21
    num_people = 7

    # Calculate the total number of desserts
    total_desserts = num_cookies + num_candy + num_brownies

    # Calculate how many desserts each person will get
    num_per_person = total_desserts / (num_people * 3) # 3 desserts per person

    result = num_per_person
    return result

print(solution())
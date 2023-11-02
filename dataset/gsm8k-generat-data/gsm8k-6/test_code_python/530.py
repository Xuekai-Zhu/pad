def solution():
    # Calculate the total number of desserts
    total_desserts = 42 + 63 + 21  # cookies + candy + brownies

    # Calculate the number of desserts each person gets
    desserts_per_person = total_desserts / (7 * 3)  # divide by number of people and types of desserts (cookies, candy, brownies)
    result = desserts_per_person
    return result

print(solution())
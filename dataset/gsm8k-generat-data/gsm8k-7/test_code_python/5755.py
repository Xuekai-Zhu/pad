def solution():
    tanya_age = 60
    john_age = tanya_age / 2
    mary_age = john_age / 2

    # Calculate the average age of all three people
    average_age = (john_age + mary_age + tanya_age) / 3
    result = average_age
    return result

print(solution())
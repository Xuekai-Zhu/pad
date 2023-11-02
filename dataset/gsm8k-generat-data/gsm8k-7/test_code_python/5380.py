def solution():
    hugh_candy = 8
    tommy_candy = 6
    melany_candy = 7

    # Calculate the total amount of candy
    total_candy = hugh_candy + tommy_candy + melany_candy

    # Divide the total amount of candy by the number of people to find the amount each person will have
    num_people = 3
    candy_per_person = total_candy / num_people
    result = candy_per_person
    return result

print(solution())
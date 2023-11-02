def solution():
    total_people = 220
    vanilla_percentage = 0.2

    # Calculate the number of people who ordered vanilla ice cream
    vanilla_people = total_people * vanilla_percentage

    # Calculate the number of people who ordered chocolate ice cream
    chocolate_people = (total_people - vanilla_people) / 3

    result = chocolate_people
    return result

print(solution())
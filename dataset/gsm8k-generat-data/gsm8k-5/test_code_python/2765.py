def solution():
    total_people = 220  # 220 people ordered ice cream on Saturday
    vanilla_percentage = 0.2  # 20% of people ordered vanilla ice cream

    # Calculate the number of people who ordered vanilla ice cream
    vanilla_people = total_people * vanilla_percentage

    # Calculate the number of people who ordered chocolate ice cream
    chocolate_people = (total_people - vanilla_people) / 3  # Vanilla ice cream orders were twice that of chocolate

    result = chocolate_people
    return result

print(solution())
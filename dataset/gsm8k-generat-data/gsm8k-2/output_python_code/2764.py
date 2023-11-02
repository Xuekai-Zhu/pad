def solution():
    """Saturday at the ice cream shop, there were twice as many people who ordered vanilla ice cream as ordered chocolate ice cream. If 220 people ordered ice cream on Saturday, and 20% of those ordered vanilla ice cream, how many people ordered chocolate ice cream?"""
    total_people = 220
    vanilla_percentage = 0.2
    vanilla_people = total_people * vanilla_percentage
    chocolate_people = (total_people - vanilla_people) / 3
    result = chocolate_people
    return result

print(solution())
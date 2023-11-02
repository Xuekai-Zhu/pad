def solution():
    total_people = 30 + 45  # Total number of people at Esme's school
    pizza_eaters = (2/3)*30 + (4/5)*45  # Number of people who ate pizza
    non_pizza_eaters = total_people - pizza_eaters  # Number of people who didn't eat pizza
    result = non_pizza_eaters
    return result

print(solution())
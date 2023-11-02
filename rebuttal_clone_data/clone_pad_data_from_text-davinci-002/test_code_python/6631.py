def solution():
    percentage_of_people = 20
    people = 1000
    stimulus_amount = 2000
    number_of_people = people * (percentage_of_people / 100)
    total_stimulus = number_of_people * stimulus_amount
    government_profit = total_stimulus * 5
    result = government_profit
    return result

print(solution())
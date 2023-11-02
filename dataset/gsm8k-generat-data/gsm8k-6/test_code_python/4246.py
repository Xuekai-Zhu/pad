def solution():
    # Calculate the total number of tomatoes
    tomato1 = 8  # first tomato plant bears 8 tomatoes
    tomato2 = 4 + tomato1  # second tomato plant bears 4 more tomatoes than the first
    tomato3 = 3 * (tomato1 + tomato2)  # third tomato plant bears 3 times the number of tomatoes as the first two plants combined
    tomato4 = 3 * (tomato1 + tomato2)  # fourth tomato plant bears 3 times the number of tomatoes as the first two plants combined
    total_tomatoes = tomato1 + tomato2 + tomato3 + tomato4
    result = total_tomatoes
    return result

print(solution())
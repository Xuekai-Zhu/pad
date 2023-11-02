def solution():
    sandwich_cost = 0.3
    juice_cost = 0.2
    money_available = 2.5
    sandwiches_possible = int(money_available / sandwich_cost)
    juices_possible = int(money_available / juice_cost)
    people = int(min(sandwiches_possible, juices_possible))
    result = people
    
    return result

print(solution())
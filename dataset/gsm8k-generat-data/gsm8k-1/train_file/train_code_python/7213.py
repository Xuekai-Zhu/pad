def solution():
    """Phil started his day with $40. He bought a slice of pizza for $2.75, a soda for $1.50 and a pair of jeans for $11.50. If he has nothing but quarters left of his original money, how many quarters does he now have?"""
    starting_money = 40
    cost_of_pizza = 2.75
    cost_of_soda = 1.50
    cost_of_jeans = 11.50
    money_spent = cost_of_pizza + cost_of_soda + cost_of_jeans
    money_left = starting_money - money_spent
    quarters_left = money_left / 0.25
    result = quarters_left
    return result

print(solution())
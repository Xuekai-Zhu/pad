def solution():
    """Well's mother sells watermelons, peppers, and oranges at the local store. A watermelon costs three times what each pepper costs. An orange costs 5
    less than what a watermelon cost. Dillon is sent to the store to buy 4 watermelons, 20 peppers, and 10 oranges. What's the total amount of money he will spend
    if each pepper costs 15$?"""
    pepper_cost = 15
    watermelon_cost = pepper_cost * 3
    orange_cost = watermelon_cost - 5
    total_cost = (4 * watermelon_cost) + (20 * pepper_cost) + (10 * orange_cost)
    result = total_cost
    return result

print(solution())
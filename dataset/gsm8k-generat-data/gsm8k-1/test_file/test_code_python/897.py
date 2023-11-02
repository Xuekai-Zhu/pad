def solution():
    """Calvin is making soup for his family for dinner. He has a pot with enough soup to fill four adult's bowls or eight child's bowls. He is an adult and will be eating with his adult wife and their two children. If everyone eats one bowl at a meal, how many times will each child be able to have a bowl of soup for lunch from the leftover soup?"""
    adult_bowls = 4
    child_bowls = 8
    total_bowls = adult_bowls * 2 + child_bowls * 2
    leftover_bowls = total_bowls - 4  # subtracting the bowls Calvin, his wife and their two children will eat
    leftover_child_bowls = leftover_bowls // 2  # dividing by 2 since two children will be sharing one bowl
    result = leftover_child_bowls
    return result

print(solution())
def solution():
    money = 10
    olives = 80
    olive_jar = 20
    olive_jar_cost = 1.50
    jars_needed = olives / olive_jar
    total_cost = jars_needed * olive_jar_cost
    change = money - total_cost
    result = change
    return result

print(solution())
def solution():
    johann_oranges = 60 # Johann starts with 60 oranges
    johann_oranges -= 10 # Johann eats 10 oranges
    stolen_oranges = johann_oranges / 2 # Half of the remaining oranges are stolen by Carson
    johann_oranges -= stolen_oranges # Johann's orange count is reduced by the number of stolen oranges
    johann_oranges += 5 # Carson returns 5 oranges
    result = johann_oranges
    return result

print(solution())
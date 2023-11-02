def solution():
     rent = 600
     food = rent * 3 / 5
     mortgage = food * 3
     salary = rent + food + mortgage + 2000 - (2000 * 2 / 5)
     result = salary
     return result

print(solution())
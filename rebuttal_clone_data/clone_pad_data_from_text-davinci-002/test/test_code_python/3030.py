def solution():
    puppies = 2
    money = 100
    puppy_cost = 20
    kitten_cost = 15
    kittens = (money - (puppies * puppy_cost)) / kitten_cost
    result = kittens
    return result

print(solution())
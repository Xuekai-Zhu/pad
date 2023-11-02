def solution():
    """The Grey's bought several chickens at a sale. John took 5 more of the chickens than Mary took. Ray took 6 chickens less than Mary. If Ray took 10 chickens, how many more chickens did John take than Ray?"""
    ray = 10
    mary = ray + 6
    john = mary + 5
    difference = john - ray
    result = difference
    return result

print(solution())
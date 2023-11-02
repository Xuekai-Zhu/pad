def solution():
    """Ray has 175 cents in nickels. Ray gives 30 cents to Peter, and he gives twice as many cents to Randi as he gave to Peter. How many more nickels does Randi have than Peter?"""
    ray_money = 175
    peter_money = 30
    randi_money = peter_money * 2
    remaining_money = ray_money - peter_money - randi_money
    nickels_ray_has = ray_money // 5
    nickels_peter_has = peter_money // 5
    nickels_randi_has = randi_money // 5
    nickels_remaining = remaining_money // 5
    difference = nickels_randi_has - nickels_peter_has
    
    return difference

print(solution())
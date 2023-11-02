def solution():
    """Ray has 175 cents in nickels. Ray gives 30 cents to Peter, and he gives twice as many cents to Randi as he gave to Peter. How many more nickels does Randi have than Peter?"""
    ray_cents = 175
    peter_cents = 30
    randi_cents = 2 * peter_cents
    total_given = peter_cents + randi_cents
    remaining_cents = ray_cents - total_given
    randi_nickels = randi_cents // 5
    peter_nickels = (peter_cents + remaining_cents) // 5
    difference = randi_nickels - peter_nickels
    result = difference
    return result

print(solution())
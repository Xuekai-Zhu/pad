def solution():
    
    starting_cents = 95
    peter_gives_cents = 25
    randi_gives_cents = peter_gives_cents * 2
    total_given = peter_gives_cents + randi_gives_cents
    cents_left = starting_cents - total_given
    nickels_left = cents_left // 5
    result = nickels_left
    return result

print(solution())
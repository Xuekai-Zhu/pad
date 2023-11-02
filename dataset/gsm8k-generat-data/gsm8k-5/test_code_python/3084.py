def solution():
    strawberries_per_handful = 5  # Susan picks 5 strawberries per handful
    eaten_per_handful = 1  # Susan eats 1 strawberry out of each handful

    # Calculate the number of strawberries Susan picks per handful
    picked_per_handful = strawberries_per_handful - eaten_per_handful

    basket_size = 60  # Susan's basket holds 60 strawberries
    picked_so_far = 0  # Susan hasn't picked any strawberries yet
    hands = 0  # Keep track of how many handfuls Susan has picked

    # Pick strawberries until the basket is full
    while picked_so_far < basket_size:
        # If Susan can pick a full handful, add it to the total picked
        if basket_size - picked_so_far >= strawberries_per_handful:
            picked_so_far += picked_per_handful * strawberries_per_handful
        # Otherwise, pick as many as possible and add them to the total picked
        else:
            remaining = basket_size - picked_so_far
            picked_so_far += remaining + eaten_per_handful * (remaining % strawberries_per_handful)
        hands += 1  # Increment the number of handfuls picked

    # Calculate the total number of strawberries picked
    total_picked = hands * strawberries_per_handful
    result = total_picked
    return result

print(solution())
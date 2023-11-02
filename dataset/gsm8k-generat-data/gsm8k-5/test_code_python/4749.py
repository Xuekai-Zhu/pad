def solution():
    bones_on_sunday = 35 - (1/2 * x) - 10  # Lassie received 10 bones on Sunday and half of her bones were eaten on Saturday
    x = 2 * bones_on_sunday  # Lassie started with twice the number of bones on Sunday

    result = x
    return result

print(solution())
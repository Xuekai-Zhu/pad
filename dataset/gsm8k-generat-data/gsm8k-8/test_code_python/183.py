def solution():
    # Define the initial number of birds
    initial_chickens = 300
    initial_turkeys = 200
    initial_guineafowls = 80

    # Define the daily loss of birds
    chicken_loss = 20
    turkey_loss = 8
    guineafowl_loss = 5

    # Calculate the number of birds left after a week
    days = 7
    chickens_left = initial_chickens - (chicken_loss * days)
    turkeys_left = initial_turkeys - (turkey_loss * days)
    guineafowls_left = initial_guineafowls - (guineafowl_loss * days)

    # Calculate the total number of birds left
    total_birds_left = chickens_left + turkeys_left + guineafowls_left
    result = total_birds_left
    return result

print(solution())
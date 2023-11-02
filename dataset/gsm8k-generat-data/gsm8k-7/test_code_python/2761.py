def solution():
    num_catfish = 16
    num_eels = 10

    # Calculate the number of trout that Henry catches
    num_trout = 3 * num_catfish

    # Calculate the total number of fishes before Henry returns half his catch
    total_fish = num_catfish + num_eels + num_trout

    # Calculate the number of fishes that Henry returns
    num_returned_fish = (num_trout / 2)

    # Calculate the total number of fishes after Henry returns half his catch
    total_fish_now = total_fish - num_returned_fish
    result = total_fish_now
    return result

print(solution())
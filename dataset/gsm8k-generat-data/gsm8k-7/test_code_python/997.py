def solution():
    num_eyes_in_one_fish = 2
    num_eyes_given_to_dog = 2
    num_eyes_eaten_by_Oomyapeck = 22

    # Calculate the total number of eyes in all the fish they catch
    total_num_eyes = num_eyes_eaten_by_Oomyapeck / (1 - (num_eyes_in_one_fish/num_eyes_given_to_dog))

    # Calculate the total number of fish they caught
    total_num_fish = total_num_eyes / num_eyes_in_one_fish

    # Calculate the number of fish each person will get to eat
    num_fish_per_person = total_num_fish / 3
    result = num_fish_per_person
    return result

print(solution())
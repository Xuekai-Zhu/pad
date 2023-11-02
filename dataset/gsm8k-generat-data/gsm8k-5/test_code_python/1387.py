def solution():
    total_gum = 54 + 45  # John and Cole have a total of 99 pieces of gum
    num_people = 3  # There are 3 people sharing the gum

    # Calculate how many pieces of gum each person gets
    num_gum_each = total_gum // num_people
    result = num_gum_each
    return result

print(solution())
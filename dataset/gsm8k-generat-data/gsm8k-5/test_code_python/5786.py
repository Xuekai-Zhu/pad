def solution():
    bags_of_buttered_popcorn = 12
    bags_of_caramel_popcorn = 10
    alan_buttered_popcorn = 3
    alan_caramel_popcorn = 1

    # Calculate the total bags of popcorn for the party
    total_popcorn = bags_of_buttered_popcorn + bags_of_caramel_popcorn

    # Calculate the bags of popcorn left after Alan takes some
    left_buttered_popcorn = bags_of_buttered_popcorn - alan_buttered_popcorn
    left_caramel_popcorn = bags_of_caramel_popcorn - alan_caramel_popcorn

    # Calculate the total bags of popcorn left for the party
    total_left_popcorn = left_buttered_popcorn + left_caramel_popcorn
    result = total_left_popcorn
    return result

print(solution())
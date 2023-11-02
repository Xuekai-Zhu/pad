def solution():
    cake_weight = 400  # The cake weights 400 grams
    parts = 8  # The cake is divided into 8 equal parts
    one_part_weight = cake_weight / parts  # Each part weighs 50 grams

    nathalie_share = one_part_weight  # Nathalie eats one-eighth of the cake
    pierre_share = 2 * nathalie_share  # Pierre eats double what Nathalie ate

    result = pierre_share
    return result

print(solution())
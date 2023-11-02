def solution():
    num_gnomes = 28
    red_hat_ratio = 0.75
    blue_hat_ratio = 1 - red_hat_ratio
    big_nose_ratio = 0.5

    num_gnomes_with_red_hats = num_gnomes * red_hat_ratio
    num_gnomes_with_blue_hats = num_gnomes * blue_hat_ratio
    num_gnomes_with_big_noses = num_gnomes * big_nose_ratio

    num_gnomes_with_blue_hats_and_big_noses = 6
    num_gnomes_with_red_hats_and_small_noses = num_gnomes_with_big_noses - num_gnomes_with_blue_hats_and_big_noses

    num_gnomes_with_red_hats_and_small_noses = round(num_gnomes_with_red_hats * (num_gnomes_with_red_hats_and_small_noses / num_gnomes_with_big_noses))

    result = num_gnomes_with_red_hats_and_small_noses
    return result

print(solution())
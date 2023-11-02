def solution():
     total_gnomes = 28
     gnomes_with_red_hats = total_gnomes * (3/4)
     gnomes_with_blue_hats = total_gnomes - gnomes_with_red_hats
     gnomes_with_big_noses = total_gnomes / 2
     gnomes_with_blue_hats_and_big_noses = gnomes_with_blue_hats / 2
     gnomes_with_red_hats_and_small_noses = gnomes_with_red_hats - gnomes_with_blue_hats_and_big_noses
     result = gnomes_with_red_hats_and_small_noses
     return result

print(solution())
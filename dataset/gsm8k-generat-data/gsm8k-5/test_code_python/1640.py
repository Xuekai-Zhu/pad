def solution():
    total_candy = 418  # They had 418 pieces of candy in total
    candy_taquon_and_mack = 171 * 2  # Taquon and Mack had 171 pieces each

    # Calculate how much candy Jafari had
    candy_jafari = total_candy - candy_taquon_and_mack
    result = candy_jafari
    return result

print(solution())
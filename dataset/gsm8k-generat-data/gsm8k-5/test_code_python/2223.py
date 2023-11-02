def solution():
    elyse_gum = 100
    rick_gum = elyse_gum / 2  # Elyse gave half of her gum to Rick
    shane_gum = rick_gum / 2  # Rick gave half of his gum to Shane
    shane_gum_left = shane_gum - 11  # Shane chewed 11 pieces of gum

    result = shane_gum_left
    return result

print(solution())
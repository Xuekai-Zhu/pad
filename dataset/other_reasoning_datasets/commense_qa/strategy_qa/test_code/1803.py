def solution():
    capricorn_parts = ["goat", "fish"]
    chimera_parts = ["lion", "goat", "snake"]
    for part in chimera_parts:
        if part not in capricorn_parts:
            result = "no"
            break
    else:
        result = "yes"
    return result

print(solution())
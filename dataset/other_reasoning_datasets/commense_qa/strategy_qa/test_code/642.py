def solution():
    small_intestine_digests = ["proteins", "carbohydrates", "fats"]
    cotton_is_cellulose = True
    if not any(item in small_intestine_digests for item in cotton_is_cellulose):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
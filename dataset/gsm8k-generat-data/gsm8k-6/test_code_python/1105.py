def solution():
    # Calculate the amount Gina gives away to her mom
    mom = (1/4) * 400

    # Calculate the amount Gina spends on clothes
    clothes = (1/8) * 400

    # Calculate the amount Gina gives to charity
    charity = (1/5) * 400

    # Calculate the amount Gina keeps
    kept = 400 - mom - clothes - charity
    result = kept
    return result

print(solution())
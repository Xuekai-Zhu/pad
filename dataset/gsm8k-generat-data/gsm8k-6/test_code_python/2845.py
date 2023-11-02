def solution():
    # Calculate the number of drops of blood required to die
    blood_loss = 3 * 5000  # 5000 drops per liter of blood
    # Calculate the number of mosquitoes required to make you lose enough blood to die
    mosquitoes_required = blood_loss / 20  # 20 drops per mosquito
    result = mosquitoes_required
    return result

print(solution())
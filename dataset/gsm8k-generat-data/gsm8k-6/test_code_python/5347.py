def solution():
    # Calculate the total earnings from selling the three types of drinks
    cola_earnings = 3 * 15  # 15 bottles of cola sold at $3 per bottle
    juice_earnings = 1.5 * 12  # 12 bottles of juice sold at $1.5 per bottle
    water_earnings = 1 * 25  # 25 bottles of water sold at $1 per bottle
    total_earnings = cola_earnings + juice_earnings + water_earnings
    result = total_earnings
    return result

print(solution())
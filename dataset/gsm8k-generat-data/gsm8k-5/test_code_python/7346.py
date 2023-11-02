def solution():
    m_to_star_ratio = 5 / 3  # Penelope has 5 M&Ms for every 3 Starbursts
    num_m = 25  # Penelope has 25 M&Ms

    # Calculate the number of Starbursts Penelope has
    num_star = (num_m / m_to_star_ratio) * (3 / 5)
    result = num_star
    return result

print(solution())
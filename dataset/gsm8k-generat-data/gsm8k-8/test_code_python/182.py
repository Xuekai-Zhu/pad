def solution():
    # Lisa's spending
    lisa_tshirt = 40
    lisa_jeans = 0.5 * lisa_tshirt
    lisa_coats = 2 * lisa_jeans

    # Carly's spending
    carly_tshirt = 0.25 * lisa_tshirt
    carly_jeans = 3 * lisa_jeans
    carly_coats = 0.25 * lisa_coats

    # Total spending
    total_spending = lisa_tshirt + lisa_jeans + lisa_coats + carly_tshirt + carly_jeans + carly_coats
    result = total_spending
    return result

print(solution())
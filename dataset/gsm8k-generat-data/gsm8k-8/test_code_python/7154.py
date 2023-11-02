def solution():
    # Calculate how many pants Alexis bought
    alexis_pants = 3 * isabella_pants

    # Calculate the total number of pants bought
    total_pants = alexis_pants + isabella_pants

    # Calculate the total number of dresses bought
    total_dresses = 18

    # Calculate the total number of pants and dresses bought by Isabella
    isabella_total = total_pants + total_dresses

    result = isabella_total
    return result

print(solution())
def solution():
    # Define the conditions given
    # Let the first and second numbers be x
    # Let the fourth number be y
    x = 2
    y = 4
    z = 0
    w = 2 * x
    u = 8 - w

    # Calculate the fifth number
    v = 8 - u

    # Calculate the zip code
    zip_code = str(x) + str(x) + str(z) + str(w) + str(v)

    result = int(zip_code)
    return result

print(solution())
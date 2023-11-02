def solution():
    """Brad’s zip code consists of five numbers that add up to 10. The first and second numbers are the same. The third number is zero. The fourth number is double the first number. The fourth and fifth numbers add up to 8. What is Brad’s zip code?"""
    # Let's use a brute force approach to solve this problem
    for i in range(10):  # First number
        for j in range(10):  # Second number
            if i == j:  # First and second numbers are the same
                for k in range(10):  # Third number
                    if k == 0:  # Third number is zero
                        for l in range(10):  # Fourth number
                            if l == 2 * i:  # Fourth number is double the first number
                                for m in range(10):  # Fifth number
                                    if l + m == 8 and i + j + k + l + m == 10:  # Fifth number and sum add up correctly
                                        result = str(i) + str(j) + str(k) + str(l) + str(m)
                                        return result

print(solution())
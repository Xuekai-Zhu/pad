def solution():
    total_fruits = 5 * 25  # The total number of fruits in all five baskets is 125
    fruits_in_a = 15  # There are 15 fruits in basket A
    fruits_in_b = 30  # There are 30 fruits in basket B
    fruits_in_c = 20  # There are 20 fruits in basket C
    fruits_in_d = 25  # There are 25 fruits in basket D

    # Calculate the number of fruits in basket E
    fruits_in_e = total_fruits - fruits_in_a - fruits_in_b - fruits_in_c - fruits_in_d
    result = fruits_in_e
    return result

print(solution())
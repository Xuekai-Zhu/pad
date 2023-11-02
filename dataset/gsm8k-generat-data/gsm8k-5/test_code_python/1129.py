def solution():
    # Calculate the amount of bronze needed for each bell
    bronze_bell1 = 50
    bronze_bell2 = 2 * bronze_bell1
    bronze_bell3 = 4 * bronze_bell2

    # Calculate the total amount of bronze needed
    total_bronze = bronze_bell1 + bronze_bell2 + bronze_bell3
    result = total_bronze
    return result

print(solution())
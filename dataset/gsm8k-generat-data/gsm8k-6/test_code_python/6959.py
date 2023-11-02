def solution():
    # Calculate the number of dolls each person has
    dolls_Debelyn = 20 - 2  # Debelyn had 20 dolls before she gave 2 to Andrena
    dolls_Christel = 24 - 5  # Christel had 24 dolls before giving 5 to Andrena
    dolls_Andrena = dolls_Debelyn + 2 + dolls_Christel + 2  # Andrena has 2 more dolls than Christel after the gifts

    # Calculate how many more dolls Andrena has than Debelyn
    more_dolls = dolls_Andrena - dolls_Debelyn
    result = more_dolls
    return result

print(solution())
def solution():
    """Debelyn, Christel, and Andrena collect dolls. Debelyn had 20 dolls before she gave Andrena 2 dolls. Christel had 24 dolls before giving Andrena 5 dolls. After all the gifts, Andrena now has 2 more dolls than Christel, how many more dolls does Andrena have now than Debelyn?"""
    # Define the initial number of dolls for each collector
    debelyn_dolls = 20
    christel_dolls = 24
    andrena_dolls = 0

    # Update the number of dolls after the gifts
    andrena_dolls += debelyn_dolls - 2
    andrena_dolls += christel_dolls - 5
    christel_dolls = andrena_dolls - 2

    # Calculate the difference between Andrena's and Debelyn's dolls
    dolls_diff = andrena_dolls - debelyn_dolls

    # Display the difference in dolls
    result = dolls_diff
    return result

print(solution())
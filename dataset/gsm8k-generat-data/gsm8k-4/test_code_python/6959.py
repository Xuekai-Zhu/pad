def solution():
    """Debelyn, Christel, and Andrena collect dolls. Debelyn had 20 dolls before she gave Andrena 2 dolls. Christel had 24 dolls before giving Andrena 5 dolls.
    After all the gifts, Andrena now has 2 more dolls than Christel, how many more dolls does Andrena have now than Debelyn?"""
    # Define the initial number of dolls for Debelyn and Christel
    debelyn_dolls = 20
    christel_dolls = 24

    # Calculate the number of dolls Andrena received from Debelyn and Christel
    andrena_received = 2 + 5

    # Update the number of dolls for Debelyn and Christel after the gifts
    debelyn_dolls -= 2
    christel_dolls -= 5

    # Calculate the total number of dolls for Andrena
    andrena_dolls = christel_dolls + 2

    # Calculate the difference in dolls between Andrena and Debelyn
    difference = andrena_dolls - debelyn_dolls

    # return the result
    result = difference
    return result

print(solution())
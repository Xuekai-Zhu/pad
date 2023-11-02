def solution():
    # Define key terms in the question
    lapidary_definition = "a person or machine who cuts gemstones"
    Dioskourides_signature = True
    portrait_of_Demosthenes = True
    # Check if Dioskourides fits the definition of a lapidary
    if lapidary_definition in "Dioskourides" and Dioskourides_signature and portrait_of_Demosthenes:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
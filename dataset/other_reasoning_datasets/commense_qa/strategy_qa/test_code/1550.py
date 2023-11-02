def solution():
    mammal = True
    mammary_tissue = True
    if mammal and mammary_tissue:
        result = "possible"
    else:
        result = "no"
    return result

# Note: Since amoebas are not mammals and do not have mammary tissue, they cannot get breast cancer. However, the wording of the question asked if they were "safe" from breast cancer, so the answer is "possible" rather than a direct "yes".

print(solution())
def solution():
    marco_rubio_religion = "Catholicism"
    worshiped_deities = ["God", "Allah"]
    if marco_rubio_religion in ["Catholicism", "Christianity"] and "Allah" not in worshiped_deities:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())
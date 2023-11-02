def solution():
    matrix_directors = ["Lilly Wachowski", "Lena Wachowski"]
    advocates_for_trans_rights = True
    if all(director.lower().endswith("wachowski") for director in matrix_directors):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
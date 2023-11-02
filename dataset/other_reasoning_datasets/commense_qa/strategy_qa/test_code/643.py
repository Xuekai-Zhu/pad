def solution():
    hippie_statement = "peace and love"
    pax_romana = "era of peace"
    augustus_loves = 3
    if pax_romana in hippie_statement and augustus_loves < 2:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
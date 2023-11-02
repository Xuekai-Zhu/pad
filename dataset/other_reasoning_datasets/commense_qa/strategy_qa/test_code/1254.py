def solution():
    politician = "Nancy Pelosi"
    political_party = "Democratic Party"
    stance_on_abortion = "pro-choice"
    if political_party == "Democratic Party" and stance_on_abortion == "pro-choice":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
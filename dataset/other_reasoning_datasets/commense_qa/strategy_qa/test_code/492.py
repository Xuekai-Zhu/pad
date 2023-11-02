def solution():
    is_lactose_intolerant = True
    dairy_avoided = True
    alternative_to_dairy = "soy milk"
    if is_lactose_intolerant and dairy_avoided:
        result = f"Yes, Cardi B would benefit from {alternative_to_dairy}."
    else:
        result = "No, Cardi B does not need an alternative to dairy milk."
    return result

print(solution())
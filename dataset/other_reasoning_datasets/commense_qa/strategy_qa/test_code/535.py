def solution():
    deicing_fluid = "Glycol"
    airlines = ["American Airlines", "United Airlines"]
    if "United Airlines" in airlines:
        result = "yes, if they fly during the winter and need de-icing fluid"
    else:
        result = "no, if they don't fly during the winter or if they use a different de-icing fluid"
    return result

print(solution())
def solution():
    disease = "bubonic plague"
    bacteria = "Yersinia pestis"
    organism = "amoebas"
    if bacteria in organism and disease == "bubonic plague":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
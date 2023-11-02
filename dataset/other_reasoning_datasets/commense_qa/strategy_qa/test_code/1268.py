def solution():
    italian_renaissance_period = [13, 14, 15, 16]
    florence_ruler = "Friar Girolamo Savonarola"
    theocracy = True
    if florence_ruler.startswith("Friar") and theocracy in italian_renaissance_period:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
def solution():
    # Calculate the amount of honey Penny purchased before tax
    honey_before_tax = (240 - 40) / 6  # subtracting minimum spend and tax, dividing by price per pound

    # Calculate the excess amount of honey purchased over the minimum spend
    excess_honey = honey_before_tax - 8  # 8 pounds is the minimum amount of honey to spend $40 before tax

    result = excess_honey
    return result

print(solution())
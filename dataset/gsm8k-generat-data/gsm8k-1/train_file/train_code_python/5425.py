def solution():
    """Michael has a chicken farm. His chickens increase in number by 150 chickens annually. If the number of chickens on his farm now is 550, how many will he have after 9 years?"""
    current_chickens = 550
    annual_increase = 150
    years = 9
    total_increase = annual_increase * years
    final_chickens = current_chickens + total_increase
    result = final_chickens
    return result

print(solution())
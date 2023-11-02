def solution():
    """Rayna has 60 more dollars than Kassidy, and Kassidy has 3/4 times as much money as Aurelia. If Aurelia has $120, how much would each have if they decided to add together their money and share equally among them?"""
    aurelia_money = 120
    kassidy_money = aurelia_money * (3/4)
    rayna_money = kassidy_money + 60
    total_money = aurelia_money + kassidy_money + rayna_money
    people = 3
    each_gets = total_money / people
    result = each_gets
    return result

print(solution())
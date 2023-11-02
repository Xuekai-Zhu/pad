def solution():
    class_one = 2300
    class_two = class_one / 2
    class_three = class_two / 8
    total_raised = class_one + class_two + class_three
    class_four = total_raised - (class_one + class_two + class_three)
    percent_deducted = 2
    administration_fee = total_raised * (percent_deducted / 100)
    amount_raised = total_raised - administration_fee
    result = amount_raised
    
    return result

print(solution())
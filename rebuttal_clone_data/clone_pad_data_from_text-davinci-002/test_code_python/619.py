def solution():
    dogs_walked_mon = 7
    dogs_walked_tues = 12
    dogs_walked_wed = 7
    dogs_walked_thurs = 9
    dogs_walked_fri = 7
    pay_per_dog = 5
    total_pay_mon = dogs_walked_mon * pay_per_dog
    total_pay_tues = dogs_walked_tues * pay_per_dog
    total_pay_wed = dogs_walked_wed * pay_per_dog
    total_pay_thurs = dogs_walked_thurs * pay_per_dog
    total_pay_fri = dogs_walked_fri * pay_per_dog
    result = total_pay_mon + total_pay_tues + total_pay_wed + total_pay_thurs + total_pay_fri
    
    return result

print(solution())
def solution():
    """A busy restaurant is counting how many customers they had during that Friday to try to predict how many they might get on Saturday. During breakfast, they had 73 customers. During lunch, they had 127 customers. During dinner, they had 87 customers. If they predict they'll get twice the amount of customers on Saturday as they had on Friday, how many customers do they predict they will get?"""
    friday_customers = 73 + 127 + 87
    saturday_customers = friday_customers * 2
    result = saturday_customers
    return result

print(solution())
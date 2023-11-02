def solution():
    """Mark has 30 candies, Peter has 25 candies, and John has 35 candies. They decided to combine their candies together and share them equally. How many candies will each one of them have?"""
    total_candies = 30 + 25 + 35
    each_candy = total_candies // 3
    result = each_candy
    return result

print(solution())
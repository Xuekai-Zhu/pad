def solution():
    """Bob and Johnny have a leaf raking business. They charge $4 for each bag of leaves they rake. On Monday they raked 5 bags of leaves. On Tuesday they raked 3 bags of leaves. On Wednesday, they counted their money and found they had $68 for all three days. How many bags of leaves did they rake on Wednesday?"""
    monday_bags = 5
    tuesday_bags = 3
    total_bags = monday_bags + tuesday_bags
    total_money = 68
    total_money_so_far = total_bags * 4
    wednesday_money = total_money - total_money_so_far
    wednesday_bags = wednesday_money / 4
    result = wednesday_bags
    return result

print(solution())
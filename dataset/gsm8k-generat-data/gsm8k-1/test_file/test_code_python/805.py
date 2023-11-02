def solution():
    """Dale is selling butterscotch candies to raise money for his club at school. He doesn't have the candies yet and is instead just taking orders. He started off with 100 total that he ordered and wanted to sell, but he ended up selling 150 butterscotch candies. Then he ordered 100 more. How many does Dale still need to sell to sell all of his candy?"""
    initial_order = 100
    sold_already = 150
    additional_order = 100
    total_order = initial_order + additional_order
    remaining_candies = total_order - sold_already
    result = remaining_candies
    return result

print(solution())
def solution():
    """Duke was at a garage sale when he spotted DVDs on sale. They were separated by price into 2 different boxes. In the first box, he found 10 movies that he wanted. These were $2.00 apiece. The second box was marked $5 each and he found 5 movies he wanted. What was the average price of each of the DVDs he bought?"""
    first_box_price = 2
    first_box_count = 10
    second_box_price = 5
    second_box_count = 5
    total_cost = (first_box_price * first_box_count) + (second_box_price * second_box_count)
    total_count = first_box_count + second_box_count
    avg_price = total_cost / total_count
    result = avg_price
    return result

print(solution())
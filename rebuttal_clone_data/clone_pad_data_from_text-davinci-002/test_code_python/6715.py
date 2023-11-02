def solution():
    Christine_first_throw = 20
    Janice_first_throw = Christine_first_throw - 4
    Christine_second_throw = Christine_first_throw + 10
    Janice_second_throw = Janice_first_throw * 2
    Christine_third_throw = Christine_second_throw + 4
    Janice_third_throw = Janice_second_throw + 17
    higher_throw = max(Christine_third_throw, Janice_third_throw)
    result = higher_throw
    return result

print(solution())
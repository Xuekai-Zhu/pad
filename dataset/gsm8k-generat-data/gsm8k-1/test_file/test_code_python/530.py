def solution():
    """Twenty kids went out on a school trip. In one of the several activities they participated in, they were divided into two equal groups of girls and boys and then went out for a scavenger hunt of seashells. The boys went out for the search and brought back 60 shells each. If the girls brought an amount equal to the number of shells brought by the boys plus four times as many seashells as the boys, how many seashells were brought by each girl?"""
    total_kids = 20
    boys = total_kids // 2
    girls = total_kids // 2
    boys_shells = 60
    girls_shells = boys_shells + (4 * boys_shells)
    seashells_per_girl = girls_shells / girls
    result = seashells_per_girl
    return result

print(solution())
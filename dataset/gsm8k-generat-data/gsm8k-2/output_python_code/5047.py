def solution():
    """Jessie won 3 times as many athletic awards as his buddy Scott, who won 4 awards. The best athlete at the rival high school won twice as many awards as Jessie. How many awards did the rival win?"""
    scott_awards = 4
    jessie_awards = 3 * scott_awards
    rival_awards = 2 * jessie_awards
    total_awards = scott_awards + jessie_awards + rival_awards
    result = rival_awards
    return result

print(solution())
def solution():
    """Kaylin is five years younger than Sarah, who is twice as old as Eli, who is nine years older than Freyja. If Freyja is ten years old, how old is Kaylin?"""
    freyja_age = 10
    eli_age = freyja_age + 9
    sarah_age = eli_age * 2
    kaylin_age = sarah_age - 5
    result = kaylin_age
    return result

print(solution())
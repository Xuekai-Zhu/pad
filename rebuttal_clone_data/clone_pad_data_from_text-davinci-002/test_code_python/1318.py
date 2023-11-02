def solution():
    charlene_to_janet = 62
    charlene_to_pablo = 70
    pablo_to_ruby = 2
    ruby_to_janet = charlene_to_janet - (charlene_to_pablo + pablo_to_ruby)
    result = ruby_to_janet
    return result

print(solution())
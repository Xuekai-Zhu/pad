def solution():
    """Mark and Peter dug ponds in their backyards. Mark's pond is 4 feet deeper than 3 times Peter's pond. If Mark's pond is 19 feet deep, what is the depth of Peter's pond?"""
    mark_depth = 19
    peter_depth = (mark_depth - 4) / 3
    result = peter_depth
    return result

print(solution())
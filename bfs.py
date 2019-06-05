def breadth_first_search(problem, candidates):
    if not candidates:
        return  # make sure there is something in the candidate list
    # I am modifying ’candidates’ list here. # Why don’t I need to copy?
    c = candidates.pop(0)  # pop from front
    node = c[-1]  # must exist
    if problem.goal(node):
        return c  # base case
    for s in problem.succ(node):
        candidates.append(c + [s])  # 1-step extension
    return breadth_first_search(problem, candidates)

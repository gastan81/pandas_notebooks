# One step at time builds the shining path
def intersect(a, b):
    intersect = set()
    set_a = set(a)
    set_b = set(b)
    for a in set_a:
        for b in set_b:
            if a == b:
                intersect.add(a)
    return intersect

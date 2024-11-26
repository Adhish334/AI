def is_variable(term):
    return isinstance(term, str) and term[0].isupper()

def occurs_check(var, term, subs):
    term = subs.get(term, term)
    if var == term:
        return True
    elif isinstance(term, tuple):
        return any(occurs_check(var, subs.get(arg, arg), subs) for arg in term[1])
    return False

def apply_subs(term, subs):
    if isinstance(term, str):
        return subs.get(term, term)
    elif isinstance(term, tuple):
        return (term[0], [apply_subs(arg, subs) for arg in term[1]])
    return term

def unify(term1, term2, subs=None):
    if subs is None:
        subs = {}
    term1 = apply_subs(term1, subs)
    term2 = apply_subs(term2, subs)
    if term1 == term2:
        return subs
    elif is_variable(term1):
        if occurs_check(term1, term2, subs):
            return None
        subs[term1] = term2
        return subs
    elif is_variable(term2):
        if occurs_check(term2, term1, subs):
            return None
        subs[term2] = term1
        return subs
    elif isinstance(term1, tuple) and isinstance(term2, tuple):
        if term1[0] != term2[0] or len(term1[1]) != len(term2[1]):
            return None
        for arg1, arg2 in zip(term1[1], term2[1]):
            subs = unify(arg1, arg2, subs)
            if subs is None:
                return None
        return subs
    return None

term1 = ("f", ["X", "a"])
term2 = ("f", ["b", "a"])

result = unify(term1, term2)
if result is not None:
    print("Unified successfully:", result)
else:
    print("Unification failed.")

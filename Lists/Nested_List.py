# Utility to flatten arbitrarily nested lists (handles tuples too).
nested_list = [1, [2, [3, 4], 5], ["a", ["b", "c"]]]
def flatten(lst):
    out=[]
    for x in lst:
        if isinstance(x,list):
            out.extend(flatten(x))
        else:
            out.append(x)
    return out

if __name__=='__main__':
    print("Nested :", nested_list)
    print("Flattened :", flatten(nested_list))
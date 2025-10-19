# Create a list with duplicates and show how to get unique values preserving order.

list=[1,5,5,3,2,3,2,4,6]
def unique_preserve_order(lst):
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

if __name__ == '__main__':
    print("Original:",list)
    print("Unique (order preserved):", unique_preserve_order(list))
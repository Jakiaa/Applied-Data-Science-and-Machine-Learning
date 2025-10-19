# A list that contains mixed data types.
mixed_list=[23, "hello", 3.25, True, None]
def describe_list(lst):
    return [(type(x).__name__,x) for x in lst]

if __name__=="__main__":
    print("Mixed List Descriptions: ", describe_list(mixed_list))
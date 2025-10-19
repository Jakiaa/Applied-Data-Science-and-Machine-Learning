#List operations on integer data and make a simple function
int_list=[15,6,8,9,23,25]
def sum_int(lst):
    """Return the total sum"""
    return sum(lst)
if __name__ == '__main__':
  print("Integer List: ", int_list)
  print("Sum: ", sum_int(int_list))
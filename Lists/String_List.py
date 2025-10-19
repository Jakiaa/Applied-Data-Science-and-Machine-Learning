#String list and function that joins them
string_list=['apple','banana','cherry']

def join_with_comma(lst):
    return ','.join(lst)

if __name__ == '__main__':
    print("String: ", string_list)
    print('Joined: ', join_with_comma(string_list))
# Count the frequency of elements using a dictionary.

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq={}
for x in words:
    freq[x]=freq.get(x,0)+1

if __name__ == '__main__':
    print("Word frequencies:", freq)
def merge_the_tools(string, k):
    # your code goes here
    # print(string,k)
    new = [string[i:i+k:] for i in range(0, len(string), k)]
    for i in new:
        s=''
        for j in i:
            if j not in s:
                s+=j
        print(s)


if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)
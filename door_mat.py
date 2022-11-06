"""It's an concise version of design door mat problem in hacker rank
which can be easily understood. Keep in mind round() function is used here..."""




#row and column argument are passed
def func(row, column):

    mid = row//2
    for i in range(round(mid) + 1):         #round built-in function is used to round the floating result
        if i == mid:
            print(("WELCOME").center(column, "-"))
        else:
            print((".|." * (2*i + 1)).center(column, "-"))
    for j in range(mid, 0, -1):
        print((".|."* (2 * j - 1)).center(column, '-'))
        

if __name__ == "__main__":
    row, column = map(int, input().split(' '))  #map function convert each element of input to "int"
    func(row, column)
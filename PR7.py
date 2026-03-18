# word_one = input("Enter a word: ")
# print(20*'-')
# reverse_word_one = list(word_one)
# reverse_word_one.reverse()
# print("-".join(reverse_word_one))





def generate_pascals_triangle(num):
    mat = []
    if(num<=2):
        if num == 1:
            print([[1]])
        if num == 2:
            print([[1]*2])
    if(num >= 3):
        for i in range(1, num + 1):
            mat += [[1] * i]
        if sum(mat[1])==2:
            mat[2][1] = 2
    for i in range(2,num-1):
        if(len(mat[i])%2==1):
            b = 0
            for l in range(0,len(mat[i])//2):
                x = 0
                x += mat[i][b]
                b += 1
                x += mat[i][b]
                mat[i+1][l+1] = x
                mat[i+1][-(l+2)] = x
        if (len(mat[i]) % 2 == 0):
            b1 = 0
            for l1 in range(0, (len(mat[i]) // 2)-1):
                x1 = 0
                x2 = 0
                x1 += mat[i][b1]
                b1 += 1
                x2 += mat[i][b1]
                mat[i + 1][l1 + 1] = x1+x2
                mat[i + 1][-(l1 + 2)] = x1+x2
                if l1 == ((len(mat[i]) // 2)-2):
                    mat[i+1][b1+1] = x2*2
    if(num>=3):
        return mat




x = generate_pascals_triangle(5)

# print(len(x))
#
# for i in x:
#     m1 = 0
#     m2 = 1
#     for j in range(0,len(x)):
#         # [1,1,1]
#         r = x[i]
#         print(" ",end=' ')
#         m1 += 1
#         if m1 == len(x)-m2:
#             # [1,2,1]
#             # [1]
#             for k in r:
#                 print(k,end=' '*4)






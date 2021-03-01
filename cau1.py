arr = ['1','2','3','4','5','6','7','8','9']
arr_str = ['+', '-', '']
arr_log = ['']*9

def xuly_sum(str):
    if str[0]=='-':
        x = str.split('+')
        sum = 0
        for j in range(len(x)):
            z = x[j].split('-')
            for i in range(len(z)):
                if z[i]=='':
                    value = 0
                else:
                    value = int(z[i])
                if j==0:
                    sum -= value
                elif i==0:
                    sum += value
                else:
                    sum -= value
    else:
        x = str.split('+')
        sum = 0
        for j in range(len(x)):
            z = x[j].split('-')
            for i in range(len(z)):
                if z[i] == '':
                    value = 0
                else:
                    value = int(z[i])
                if i==0:
                    sum += value
                else:
                    sum -= value
    if sum==100:
        print(str+' = 100')


def chuoi(str):
    string = ''
    for i in range(9):
        string += str[i]
        string += arr[i]
    if string[0]!='+':
        xuly_sum(string)

def dequy(j):
    for i in range(3):
        arr_log[j]=arr_str[i]
        if j<8:
            dequy(j+1)
        if j==8:
            chuoi(arr_log)

if __name__ == '__main__':
    dequy(0)

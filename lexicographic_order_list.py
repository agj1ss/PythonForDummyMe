if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst=[[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if a + b + c != n]
    
sorted_list = sorted(lst, key = lambda i: (len(i), i)) 

print(sorted_list)

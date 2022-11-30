if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr) #convert arr into list
    scores.sort()      #sort the list in ascending order
    first, second = -100, -100  #set the min values from constraint because I don't know the input test case
    for score in scores:        #if first < score then assign it to second and assign score to first
        if first < score:
            second = first
            first = score
    print(second)

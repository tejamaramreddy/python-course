def string_compression(str1):
    count1 = {}
    r = ''
    for i in str1:
        if i in count1:
            count1[i] +=1
        else:
            count1[i] = 1
    for i in count1:
        r +=i
        r += str(count1[i])
    print(r)
    
string_compression('AAAAABBBBCCCC')
string_compression('AABBCC')
str = "   space here  "
result = ''
count = 0
str = str.strip()
words = str.split()
for i in words:
    count += 1
for i in range(count):
    result += words.pop() 
    result += ' '
print(result.strip())
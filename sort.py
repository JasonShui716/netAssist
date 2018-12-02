word=[]
while True:
    try:
        word.append(input())
    except EOFError as e:
        break;
for i in sorted(word):
        print(i)

def matchingStrings(strings, queries):
    results = {q:0 for q in queries};
    answer = []

    for q in queries:
        count = 0
        for s in strings:
            if q == s:
                count = count + 1
        answer.append(count)
    return answer

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    n = int(input().strip())

    strings = []
    for _ in range(n):
        s = input().strip()
        strings.append(s)

    q = int(input().strip())
    queries = []
    for _ in range(q):
        q = input().strip()
        queries.append(q)

    result = matchingStrings(strings, queries)
    print(result)
    fptr.write(str(result))

    fptr.close();

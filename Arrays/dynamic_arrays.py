# https://www.hackerrank.com/challenges/dynamic-array/problem

def dynamic_array(n, queries):
    arr = [None] * n

    for i in range(n):
        arr[i] = []

    answersArray = []
    lastAnswer = 0
    for query in queries:
        i = (query[1] ^ lastAnswer) % n
        if query[0] == 1:
            arr[i].append(query[2])
        elif query[0] == 2:
            lastAnswer = arr[i][query[2] % len(arr[i])]
            print(lastAnswer)
            answersArray.append(lastAnswer)

    return answersArray


if __name__ == '__main__':
    n = 2
    queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
    answers = dynamic_array(n, queries)
    print(answers)

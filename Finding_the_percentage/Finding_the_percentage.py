if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=0
    for i in student_marks[query_name]:
        a+=i
    b=a/3    
    print("%0.2f" % b)
# for query_name in student_marks[]


def doWork(query_name, student_marks):
    values = student_marks[query_name]
    print(sum(values))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n): 
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    
    values = student_marks[query_name]
    print("%.2f" % float(sum(values)/len(values)))



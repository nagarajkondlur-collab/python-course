# problem : 14 student marks analyzer
marks = (100,95,80,66,54,50,52,47,38,35,28,19,9,7,4,2,1)

def analyze_marks(marks):
    total = len(marks)
    highest = max(marks) if marks else None # highest marks yavdu fix ella andre yardu ist ali maximum marks erutto adhhe
    lowest = min(marks) if marks else None # same for low also
    average = sum(marks) / total if total else 0
    passing = sum(1 for m in marks if m >= 35)
    failing = total - passing
    return {
        'total_students': total,
        'highest_mark': highest,
        'lowest_mark': lowest,
        'average_mark': average,
        'passing_students': passing,
        'failing_students': failing,
    }

if __name__ == '__main__':
    print(analyze_marks(marks))
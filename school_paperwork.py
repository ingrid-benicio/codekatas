def paper_class(classmate, pages):
    if classmate < 0 or pages < 0:
        return 0
    else:
        return classmate * pages

print(paper_class(10,5))
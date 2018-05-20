def myrange(start=None, end=None, step=1):
    if not start:
        start = 0
        end = 0
    if not end:
        end = start
        start = 0
    num = start
    while (num < end):
        yield num
        num = num + step
t = list(myrange())
print(t)

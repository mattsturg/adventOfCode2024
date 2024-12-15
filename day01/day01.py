# Just numbers
def test(ls):
    s = 0
    for line in ls:
        first = None
        last = None
        for let in line:
            if let.isnumeric():
                last = int(let)
                if first is None:
                    first = last
        s += first*10+last
    return s

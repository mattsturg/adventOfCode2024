import re


def corrupt_mem(ls):
    total = 0
    for line in ls:
        reg = re.findall("mul\(\d+,\d+\)", line)
        for mul in reg:
            mult_clean = mul[4:len(mul) - 1].split(",")
            total += int(mult_clean[0]) * int(mult_clean[1])
    return total


def corrupt_mem_p2(ls):
    total = 0
    line = ''.join(ls)
    dos = line.split("do()")
    dont = []
    for do in dos:
        dont.append(do.split("don't()")[1:])
    do_muls = []
    dont_muls = []

    dont = sum(dont, [])
    for section in dos:
        do_muls.append(re.findall("mul\(\d+,\d+\)", section))
    for section in dont:
        dont_muls.append(re.findall("mul\(\d+,\d+\)", section))
    dont_muls = sum(dont_muls, [])
    do_muls = sum(do_muls, [])

    for dont in dont_muls:
        do_muls.remove(dont)
    for mul in do_muls:
        mult_clean = mul[4:len(mul) - 1].split(",")
        total += int(mult_clean[0]) * int(mult_clean[1])
    return total

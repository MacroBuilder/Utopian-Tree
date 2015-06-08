def utopian_tree(cycles):
    height = 1
    if cycles == 0:
        return height
    else:
        switch = False
        for i in range(cycles):
            if switch == False:
                height *= 2
                switch = True
            elif switch == True:
                height += 1
                switch = False
        return height

test_cases = int(raw_input())

for _ in range(test_cases):
    c = int(raw_input().strip())
    print utopian_tree(c)

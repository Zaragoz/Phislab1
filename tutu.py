def qsort(list):
    if len(list) < 2:
        return list
    else:
        pilot = list[0]
        smoller = [i for i in list[1:] if i <= pilot]
        biger = [i for i in list[1:] if i > pilot]
        return qsort(smoller) + [pilot] + qsort(biger)

print(qsort([1,8,3,9,4,97,4,0]))
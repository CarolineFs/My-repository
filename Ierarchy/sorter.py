# ID - Parent ID

# CONST
NULL = 0

objects = [(2, 0), (6, 2), (7, 0), (3, 2), (7, 6), (3, 0)]

# Тут пока что работает только сортировка расческой
def sorter_by_indx(array, indx):
    array_len = len(array)
    gap = (array_len*10//13) if array_len > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = 0
        for i in range(array_len - gap):
            if array[i+gap][indx] < array[i][indx]:
                array[i], array[i+gap] = array[i+gap], array[i]
                swapped = 1
        gap = (gap*10//13) or swapped
    return array


a = sorter_by_indx(objects, 0)
print(a)


'''def parents(res):
    parents = []
    for i in res:
        parents.append(i[0])
    return parents


def main(objects):
    res = []
    ind_to_pop = []
    for i in range(len(objects)):
        if objects[i][1] == NULL:
            res.append(objects[i])
            ind_to_pop.append(i)
    for i in reversed(ind_to_pop):
        objects.pop(i)
    while len(objects) > 0:
        if len(res) == 0:
            res.append(objects[0])
            objects.pop(0)
        if objects[0][1] == 0:
            res = [objects[0]] + res
            objects.pop(0)
        else:
            current_obj = [(objects[0])]
            # current_id = objects[0][0]
            current_par_id = objects[0][1]
            parents_in_res = parents(res)
            for i in range(len(parents_in_res)):
                if parents_in_res[i] == current_par_id:
                    # print(current_obj)
                    # print(res)
                    # print(i)
                    res = res[:i+1] + current_obj + res[i+1:]
                    objects.pop(0)
                    break
    print(res)

main(objects)'''

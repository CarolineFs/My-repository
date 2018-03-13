'''
У каждого объекта есть ID, NAME и PARENT ID
Скрипт, который располагает на странице объекты в виде иерархического списка
На самом деле не скрипт, а костыль
'''

# CONST
NULL = 0
OBJECT_IDX = 0
NAME_IDX = 1
PARENT_IDX = 2


# Как должно быть
'''objects = [(2, "Организация", NULL),
           (3, "Бухгалтерия", 2),
           (6, "Отдел охраны", 2),
           (7, "Караульная служба", 6),
           (8, "Бюро пропусков", 6),
           (12, "Патентный отдел", 2),
           (13, "Лётная служба", 2),
           (14, "Лётный отряд Боинг 737", 13),
           (17, "Лётный отряд Боинг 747", 13),
           (18, "1-ая авиационная эскадрилия Боинг 737", 14),
           (19, "2-ая авиационная эскадрилия Боинг 737", 14),
           (21, "Лётно-методический отдел", 13)]'''


objects = [(2, "Организация", NULL),
           (18, "1-ая авиационная эскадрилия Боинг 737", 14),
           (6, "Отдел охраны", 2),
           (7, "Караульная служба", 6),
           (8, "Бюро пропусков", 6),
           (13, "Лётная служба", 2),
           (12, "Патентный отдел", 2),
           (17, "Лётный отряд Боинг 747", 13),
           (14, "Лётный отряд Боинг 737", 13),
           (19, "2-ая авиационная эскадрилия Боинг 737", 14),
           (21, "Лётно-методический отдел", 13),
           (3, "Бухгалтерия", 2)]


def sorter_by_indx(array, indx):
    array_len = len(array)
    gap = (array_len*10//13) if array_len > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = 0
        for i in range(array_len - gap):
            if array[i+gap][indx] > array[i][indx]:
                array[i], array[i+gap] = array[i+gap], array[i]
                swapped = 1
        gap = (gap*10//13) or swapped
    return array


def main(objects):
    objects = sorter_by_indx(objects, OBJECT_IDX)
    objects = sorter_by_indx(objects, PARENT_IDX)
    res = []
    k = len(objects) - 1
    while objects[k][PARENT_IDX] == NULL:
        res.append(objects[k])
        k -= 1
    objects = sorter_by_indx(objects, OBJECT_IDX)
    while len(objects) > 0:
        if len(res) == 0:
            res.append(objects[0])
            objects.pop(0)
        if objects[0][PARENT_IDX] == NULL:
            objects.pop(0)
        else:
            current_obj = [(objects[0])]
            current_par_id = objects[0][PARENT_IDX]
            for i in range(len(objects)):
                if objects[i][PARENT_IDX] == current_par_id:
                    res = res[:i+1] + current_obj + res[i+1:]
                    objects.pop(0)
                    break
    return res


objects = main(objects)

coefficient = 1  # количество пробелов, короче
for i in range(len(objects)):
    if objects[i][PARENT_IDX] == NULL:
        coefficient = 1
    else:
        if objects[i][PARENT_IDX] > objects[i-1][PARENT_IDX]:
            coefficient += 4
        if objects[i][PARENT_IDX] < objects[i-1][PARENT_IDX]:
            coefficient -= 4
    print(coefficient*' ' + objects[i][NAME_IDX])


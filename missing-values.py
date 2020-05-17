def find_missing_values(lst1,lst2):
    for i in lst1:
        if i not in lst2:
            print(i)
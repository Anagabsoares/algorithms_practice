# Linear search = O(n) time complexity->  

##### It checkes each element in a list - one at a time. 
>The number of operations grows (time) as the number of elements in the list increases.

>def check_value(lista:list(), value:int) -> int:
    for item in lista:
        if item == value:
            return lista.index(item)
    return -1
    
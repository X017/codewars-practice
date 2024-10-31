

def find_outlier(integers):
    even_arr = []
    odd_arr = []
    
    for i in integers:
        if i % 2 == 0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
        
    if len(even_arr) == 1:
        return even_arr[0]
    else:
        return odd_arr[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
    
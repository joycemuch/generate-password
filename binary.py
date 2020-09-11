

def bin_sort(list_l , e):
     last_index = int(len(list_l)-1)
     start_index = 0
     middle_index = 0
     list_l.sort()
     while True: 

        middle_index = (start_index + last_index)//2
       
        if list_l[middle_index ]< e:
                last_index = middle_index +1
        
        elif list_l[middle_index] > e:
                start_index = middle_index
        elif e == list_l[middle_index]:
            return print("element has been found at index  {}  ".format(middle_index))
            
     return print("element has  not been found ")

if __name__=="__main__":
    a = [1, 3, 5, 30, 42, 43, 500] 

bin_sort (a ,30)


 



def heappush(heap, n) :
    heap.append(n)         
    i = len(heap)-1       
    while i != 1 :          
        pi = i//2           
        if n >= heap[pi]:  
            break
        heap[i] = heap[pi]  
        i = pi            
    heap[i] = n 


def heappop(heap) :
    size = len(heap) - 1    # 노드의 개수
    if size == 0 :          
        return None
    root = heap[1]         
    last = heap[size]       
    pi = 1                  
    i = 2                   
    while (i <= size):      

        if i<size and heap[i] > heap[i+1]:  
            i += 1          

        if last <= heap[i]:
            break
        heap[pi] = heap[i]  
        pi = i              
        i *= 2
    heap[pi] = last         
    heap.pop()             

    return root 



def make_tree(text) :
    heap = [0]
    for n in freq.values() :
        heappush(heap, n)
    for i in range(1, len(freq)) :
        e1 = heappop(heap)
        e2 = heappop(heap)
        heappush(heap, e1 + e2)
        print("(%d + %d)" %(e1, e2))
 
freq={'k':10, 'o':5, 'r':2, 'e':15, 'a':18, 't':4, 'c':7, 'h':11}
  
text = input("Please a word: ")
make_tree(text)
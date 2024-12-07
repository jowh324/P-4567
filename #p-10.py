#p-10
class data:
    def __init__(self):
        self.comparisons=0 #비교
        self.move=0 #이동
        
    #비교, 이동 리셋
    def reset(self):
        self.comparisons=0 
        self.move=0 
        
class Algo:
    def __init__(self):
        self.data= data()
        
    def  Selection(self,arr):
        n= len(arr)
        for i in range(n-1):
            min_index=i
            for j in range(i+1,n):
                self.data.comparisons +=1
                if arr[j] <arr[min_index]:
                    min_index = j
            arr[i],arr[min_index]= arr[min_index],arr[i]
            self.data.move +=2        
    
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                self.data.comparisons += 1
                arr[j + 1] = arr[j]
                self.data.move += 1
                j -= 1
            arr[j + 1] = key
            self.data.move += 1
    
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.data.comparisons += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.data.move += 2
    
    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    self.data.comparisons += 1
                    arr[j] = arr[j - gap]
                    self.data.move += 1
                    j -= gap
                arr[j] = temp
                self.data.move += 1
            gap //= 2
            
    def merge_sort(self, arr):
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                self.data.comparisons += 1
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                    self.data.move += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return merge(left, right)

        sorted_arr = mergesort(arr)
        for i in range(len(arr)):
            arr[i] = sorted_arr[i]
    
    def quick_sort(self,arr):
        def quick(left,right):
            if left<right:
                q= partition(left,right)
                quick(left, q-1)
                quick(q+1,right)
                
        def partition(left,right):
            q = arr[left]
            i= left+1
            j= right
            while True:
                while i <= j and arr[i] <= q:
                    self.data.comparisons += 1
                    i += 1
                while i <= j and arr[j] >= q:
                    self.data.comparisons += 1
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    self.data.move += 2
                else:
                    break
            arr[left], arr[j] = arr[j], arr[left]
            self.data.move += 2
            return j
        quick(0, len(arr) - 1)
        
    def radix_sort(self, arr):
        max_value = max(arr)
        exp = 1
        while max_value // exp > 0:
            count = [0] * 10
            output = [0] * len(arr)

            for num in arr:
                index = (num // exp) % 10
                count[index] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(len(arr) - 1, -1, -1):
                index = (arr[i] // exp) % 10
                output[count[index] - 1] = arr[i]
                count[index] -= 1
                self.metrics.movements += 1

            for i in range(len(arr)):
                arr[i] = output[i]
            exp *= 10
            

#실행
algorithms=Algo()

algorithmszip={"SEL": algorithms.Selection,
        "INS": algorithms.insertion_sort,
        "BUB": algorithms.bubble_sort,
        "SHE": algorithms.shell_sort,
        "MER": algorithms.merge_sort,
        "QUI": algorithms.quick_sort,
        "RAD": algorithms.radix_sort,}

data=input("데이터 리스트 입력 : ").split(',')

data=[int(x.strip()) for x in data]

print(" Target Sorting Algorithm List")
print("Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE), Heap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")
algo_key = input("* Select sorting algorithm: ").strip().upper()

if algo_key in algorithmszip:
    algorithms.data.reset()
    sorting_algorithm = algorithmszip[algo_key]
    sorting_algorithm(data)
    
    print(f">> Sorted: {', '.join(map(str, data))}")
    print(f">> Number of Comparisons: {algorithms.data.comparisons}")
    print(f">> Number of Data Movements: {algorithms.data.move}")
    
else:
    print("사용할 수 없는 알고리즘")
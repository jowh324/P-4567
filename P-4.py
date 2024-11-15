class CircularQueue:
    def __init__(self,capacity=10) :
        self.capacity=capacity
        self.array=[None]*capacity
        self.front = 0
        self.rear = 0
        
    def isEmpty(self):
        return self.front ==self.rear
    
    def isFull(self):
        return self.front ==(self.rear+1)%self.capacity
    
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1) %self.capacity
            self.array[self.rear] = item
        else:pass
        
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.capacity
            return self.array[self.front]
        else:pass
        
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)]
    
    def display(self):
        i= (self.front + 1) % self.capacity
        while i !=(self.rear +1)%self.capacity:
            print(self.array[i],end='')
            i=(i+1)%self.capacity
        print()
        
q=CircularQueue(10)
while True:
    command = input("[메뉴선택] q-입력, d-삭제, m-종료=>")
    if command =='q':
       
        item = input("입력행 내용:")
        q.enqueue(item)
        q.display()
            
    elif command == 'm':
        print("프로그램을 종료합니다.")
        exit()
    
    elif command == 'd':
        q.dequeue()
        q.display()
    
    
        
        
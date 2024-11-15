class BSTNode:
    
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None

    def search_bst(n,key):
        if n==None:
            return None
        elif key == n.key:
            return n
        elif key <n.key:
            return BSTNode.search_bst(n.left,key)
        else:
            return BSTNode.search_bst(n.right,key)
    
    def search_min_bst(n):
        while n !=None and n.left !=None:
            n=n.left
        return n
    
    def search_value_bst(n,value):
        if n==None: return None
        elif value==n.value:
            return n
        res = BSTNode.search_value_bst(n.left,value)
        if res is not None:
            return res
        else: 
            return BSTNode.search_value_bst(n.right,value)
        
    def search_max_bst(n):
        while n !=None and n.right !=None:
            n=n.right
        return n

    def insert_bst(root,node):
        if root==None:
            return node
        
        if node.key == root.key:
            return root 
        
        if node.key <root.key:
            root.left = BSTNode.insert_bst(root.left,node)
        else: 
            root.right= BSTNode.insert_bst(root.right,node)
            
        return root
    
    def delete_bst(root,key):
        if root ==None:
            return root
        
        if key< root.key:
            root.left =BSTNode.delete_bst(root.left,key)
        elif key>root.key:
             root.right =BSTNode.delete_bst(root.right,key)
             
        else:
            if root.left==None:
                return root.right
            if root.right==None:
                return root.left
            succ=BSTNode.search_min_bst(root.right)
            root.key =succ.key
            root.value=succ.value
            root.right=BSTNode.delete_bst(root.right,succ.key)
        return root



class BSTMap():
    def __init__(self):
        self.root=None
    def isEmpty (self):
        return self.root==None
    
    def findMax(self):
        return BSTNode.serch_max_bst(self.root)
    
    def findMin(self):
        return BSTNode.serch_min_bst(self.root)
    
    def search(self,key):
        return BSTNode.search_bst(self.root,key)
    def sarchValue(self, value):
        return BSTNode.search_value_bst(self.root,value)
    
    def insert(self,key,value):
        n=BSTNode(key,value)
        self.root=BSTNode.insert_bst(self.root,n)
    
    def delete(self,key):
        self.root=BSTNode.delete_bst(self.root,key)
       
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    # 전위 순회 (Preorder)
    def preorder(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    # 후위 순회 (Postorder)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=' ')

    def display(self, msg='BST Map:', order=1):
        print(msg, end=': ')
        if order == 1:  # Inorder
            self.inorder(self.root)
        elif order == 2:  # Preorder
            self.preorder(self.root)
        elif order == 3:  # Postorder
            self.postorder(self.root)
        print()  # 줄바꿈
        
bst_map = BSTMap()
bst_map.insert(30, 'A')
bst_map.insert(20, 'B')
bst_map.insert(40, 'C')
bst_map.insert(10, 'D')
bst_map.insert(25, 'E')

# 중위 순회
bst_map.display(order=1)

# 전위 순회
bst_map.display(order=2)

# 후위 순회
bst_map.display(order=3)
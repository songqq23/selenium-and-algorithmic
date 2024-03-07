#括号匹配,用栈实现
#只用判空、压栈、弹栈功能即可
class Stack:
    def __init__(self):
        self.lista = []#创建空栈

    def isEmpty(self):
        return len(self.lista) == 0
    def push(self,item):
        self.lista.append(item)
    def pop(self):
        if self.isEmpty():
            return "Error：The stack is empty"
        else:
            return self.lista.pop()

def matching(inputstring):#输入是一串字符
    bktStack = Stack()#创建类实例
    have_left=False
    #对于每个输入字符
    for index,i in enumerate(inputstring):
        #遇到左括号，就将其压栈
        if i=='(':
            bktStack.push(index)
            have_left = True
        #遇到右括号
        elif i==')':
            #若已没左括号与之匹配
            if bktStack.isEmpty() or not have_left:
                bktStack.push(index)
                have_left=False
            elif have_left:
                bktStack.pop()
    arr = [' ' for i in range(len(inputstring))]
    while not bktStack.isEmpty():
        index2=bktStack.pop()
        if inputstring[index2]=='(':
            arr[index2]='x'
        elif inputstring[index2]==')':
            arr[index2]='?'
    s=''.join(arr)
    print(inputstring)
    print(s)
#测试函数
stringa = input()
matching(stringa)

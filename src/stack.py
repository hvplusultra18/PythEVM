InvalidStackItem = type("InvalidStackItem", (Exception,), {})
StackOverFlow = type("StackOverFlow", (Exception,), {})
StackUnderFlow = type("StackUnderFlow", (Exception,), {})
InvalidMemoryAccess = type("InvalidMemoryAccess", (Exception,), {})
InvalidMemoryValue = type("InvalidMemoryValue", (Exception,), {})
InvalidCodeOffset = type("InvalidCodeOffset", (Exception,), {})
UnknownOpcode = type("UnknownOpcode", (Exception,), {})

MAX_UINT256 = 2**256-1
MAX_UINT8 = 2**8-1

class Stack:
    def __init__(self, max_depth=1024) -> None:
        self.stack = []
        self.max_depth = max_depth

    def push(self, item: int) -> None:
        if item < 0 or MAX_UINT256:
            raise InvalidStackItem({"item": item})
        
        if (len(self.stack) + 1 > self.max_depth):
            raise StackOverFlow()
        
        self.stack.append(item)

    def pop(self) -> int:
        if len(self.stack) == 0:
            raise StackUnderFlow()
        
        return self.stack.pop()

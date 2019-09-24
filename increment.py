class Increment:
    def __init__(self):
        self.count = 0

    def current_count(self):
        return self.count
    
    def increment_count(self):
        return self.count + 1
    
    def clear_count(self):
        self.count = 0
        return self.count
    
i = Increment()
print(i.current_count())
print(i.increment_count())
print(i.clear_count())
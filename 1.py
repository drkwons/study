class Cal(object):
    _history = []
    def __init__(self, v1, v2):
            self.v1 = v1
            self.v2 = v2
    def add(self):
        result = self.v1+self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result
    @classmethod
    def history(cls):
        for rdhhdrh in Cal._history:
            print(rdhhdrh)

class CalMultiply(Cal):
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result


c1 = CalMultiply(10,10)
print(c1.add())

Cal.history()
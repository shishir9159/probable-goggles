from quickest_copy import Solution

def main():
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    print(solution.subsets(nums))

from inspect import isfunction, isdatadescriptor, isclass

def separate_members(classDict):
    d = dict(methods=[], properties=[], other=[])

    for k, v in list(classDict.items()):
        if isfunction(v):
            d['methods'].append(k)
        elif isdatadescriptor(v):
            d['properties'].append(k)
        elif not isclass(v):
            d['other'].append(k)

    return d

class __printer__(type):
    def __new__(meta, classname, bases, classDict):
        d = separate_members(classDict)

        for k, v in list(d.items()):
            print('%s:' % k)
            for name in v:
                print('- %s' % name)
            print('-'*80)

        return type.__new__(meta, classname, bases, classDict)

class Test(object, metaclass=__printer__):
    a = 47
    b = 'raspberry'
    def c(self): pass
    d = property(lambda self: None)
    e = 45.67
    f = [23, 24, 25]
    g = lambda self: None
    def h(self, v): self.v = v
    i = property(c, h)

if __name__ == "__main__":
    Test()
    # main()
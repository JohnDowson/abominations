class IntWithTimes(int):

    def times(self, codestring=None, _locs={}):
        _glob = globals()
        if codestring:
            for _t_ in range(self):
                exec(codestring, _glob, _locs)
            return self
        else:
            return range(self)

class ListWithEach(list):
    def each(self, codestring):
        _glob = globals()
        for _t_ in self:
            exec(codestring, _glob, {'item':_t_})
        return self

    def each_with_object(self, codestring, obj):
        _glob = globals()
        for _t_ in self:
            exec(codestring, _glob, {'item':_t_, 'acc':obj})
        return obj

    def reduce(self, codestring, obj):
        _glob = globals()
        for _t_ in self:
            _results = []
            for line in codestring.split('\n'):
                _result = (eval(codestring, _glob, {'item':_t_, 'acc':obj}))
                if _result: _results.append(_result)
            if isinstance(obj, int): obj = _results[-1]
            elif isinstance(obj, str): obj.join(str(result))
            else: obj.append(_results[-1])
        return obj

if __name__ == "__main__":

    a = IntWithTimes(2)
    a.times(
"""print("hello there general kenobi")
print("1+1")""")

    b = ListWithEach([1,2,"hello",4])
    b.each(
"""print(f\"item was {item}\")
IntWithTimes(2).times(\"print(item, item)\", locals())
print(f\"item is now {item}\")""")

    c = ListWithEach(a.times())
    print(c)
    print(c.each_with_object("""acc.append(item + 2)""", []))
    print(c)
    d = ListWithEach([1,2,3])
    print(d.each_with_object("""acc+=item""", 1))
    print(d)
    print(d.reduce(
"""acc+item
""", 1))
    print(d.reduce(
"""item
""", 1))

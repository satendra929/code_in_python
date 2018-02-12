elements = ["H","H","V","V"]
ele = "1234"
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

@Memoize
def generate_per(elements,length) :
    if length == 1 :
        return  elements
    else :
        ret_res = []
        for i in range (len(elements)) :
            for r in generate_per(elements[:i]+elements[i+1:],length-1) :
                ret_res.append(elements[i] + r)
        return ret_res

generate_combi = Memoize(generate_per)
print generate_per(ele,4)

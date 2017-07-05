import random
class DigitTransformer:
    l_list= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
             'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
             'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', 
             '8', '9']
        
    def __init__ (self, number, to_bit_depth=52, shift=0):
        alist = []
        if abs(shift)>len(DigitTransformer.l_list):
            shift%=len(DigitTransformer.l_list)
        string =''
        mark = ''
        if number<0:
            mark = '-'
            number = -number
        while number!=0:
            alist+= [number%to_bit_depth]
            number//=to_bit_depth
        iter = reversed(alist)
        while iter.__length_hint__() != 0:
            iter_i = iter.__next__()+shift
            if iter_i>=len(DigitTransformer.l_list) :
                string += DigitTransformer.l_list[iter_i%len(DigitTransformer.l_list)]
            else:
                string += DigitTransformer.l_list[iter_i]
        self.shift = shift
        self.bit_depth = to_bit_depth
        self.val = mark+string
        del string, iter, mark, alist

    def dec_val(self):
        a = 0
        if self.val.startswith('-'):
            mark = '-'
            q = self.val[1:]
        else:
            q = self.val
            mark = ''
        iter = reversed(list(q))
        alist = []
        while iter.__length_hint__() !=0 :
            iter_i = DigitTransformer.l_list.index(iter.__next__())-self.shift
            if iter_i<0:
                iter_i+=len(DigitTransformer.l_list)
            alist.append(iter_i*(self.bit_depth**a))
            a += 1
        if mark=='-':
            res = -sum(alist)
        else:
            res = sum(alist)
        return res

    def __add__(self, other):
        try:
            if self.bit_depth == other.bit_depth:
                res = DigitTransformer(self.dec_val() + other.dec_val(), self.bit_depth)
            else:
                res = DigitTransformer(self.dec_val() + other.dec_val())
        except AttributeError:
            res = DigitTransformer(self.dec_val() + other, self.bit_depth, self.shift)
        return res

    def __sub__(self, other):
        try:
            if self.bit_depth == other.bit_depth:
                res = DigitTransformer(self.dec_val() - other.dec_val(), self.bit_depth)
            else:
                res = DigitTransformer(self.dec_val() - other.dec_val())
        except AttributeError:
            res = DigitTransformer(self.dec_val() - other, self.bit_depth, self.shift)
        return res
    
    @staticmethod
    
    def from_string(string, bit_depth=52, shift=0):
        if string.startswith('-'):
            mark = '-'
            string = string[1:]
        else:
            mark = ''
        iter = reversed(list(string))
        alist = []
        a = 0
        while iter.__length_hint__() !=0 :
            iter_i = DigitTransformer.l_list.index(iter.__next__())-shift
            if iter_i<0:
                iter_i+=len(DigitTransformer.l_list)
            alist.append(iter_i*(bit_depth**a))
            a += 1
        if mark == '-':
            res = -sum(alist)
        else:
            res = sum(alist)
        return DigitTransformer(res, bit_depth, shift)

class Element:
    order_dict = 1
    def __init__(the_order, key, location):
        
import random
class Digit_Transformer:
    l_list= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
             'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
             'w', 'x', 'y', 'z', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 
             'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 
             'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 
             'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 
             'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 
             'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ']
    list_for_shift = [i for i in range(116)]
    
    def __init__ (self, number, to_bit_depth=116, shift=0):
        alist = []
        string =''
        mark = ''
        if number<0:
            mark = '-'
            number = abs(number)
        while number!=0:
            alist+= [number%to_bit_depth]
            number//=to_bit_depth
        iter = reversed(alist)
        while iter.__length_hint__() != 0:
            string += Digit_Transformer.l_list[Digit_Transformer.list_for_shift[iter.__next__()+shift]]
        self.shift = shift
        self.bit_depth = to_bit_depth
        self.val = mark+string
        del string, iter,mark

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
            alist.append((Digit_Transformer.l_list.index(iter.__next__())-self.shift)*(self.bit_depth**a))
            a+=1
        if mark=='-':
            res = -sum(alist)
        else:
            res = sum(alist)
        return res

    def __add__(self, other):
        if self.bit_depth == other.bit_depth:
            res = Digit_Transformer(self.dec_val()+other.dec_val(), self.bit_depth)
        else:
            res = Digit_Transformer(self.dec_val()+other.dec_val())
        return res

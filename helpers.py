pairing = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

class Helper:
    def createNewPatent(self,l1,l2,l3,l4,n):
            if n < 999:
                m = n + 1
                if m < 10:
                    m = '00' + str(m)
                elif m < 100:
                    m = '0' + str(m)
                else:
                    m = str(m)
                NewPatent = self.get_key(l1) + self.get_key(l2) + self.get_key(l3) + self.get_key(l4) + m
                return NewPatent
            else:
                if l4 < 26:
                    l4 += 1
                    m = '000'
                    NewPatent = self.get_key(l1) + self.get_key(l2) + self.get_key(l3) + self.get_key(l4) + m
                    return NewPatent
                else:
                    if l3 < 26:
                        l4 = 1
                        l3 += 1
                        m = '000'
                        NewPatent = self.get_key(l1) + self.get_key(l2) + self.get_key(l3) + self.get_key(l4) + m
                        return NewPatent
                    else:
                        if l2 < 26:
                            l4 = 1
                            l3 = 1
                            l2 += 1
                            m='000'
                            NewPatent = self.get_key(l1) + self.get_key(l2) + self.get_key(l3) + self.get_key(l4) + m
                            return NewPatent
                        else:
                            if l1 < 26:
                                l4 = 1
                                l3 = 1
                                l2 = 1
                                l1 += 1
                                m = '000'
                                NewPatent = self.get_key(l1) + self.get_key(l2) + self.get_key(l3) + self.get_key(l4) + m
                                return NewPatent
                            else:
                                return "Finish"

    def get_key(self, val):
        for key, value in pairing.items():
            if val == value:
                return key
        return "key doesn't exist"
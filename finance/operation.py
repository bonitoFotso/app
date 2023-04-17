def total(self):
    s=0
    for i in self.model.objects.all() :
        s = s+i.montant
    return s
    
def ex_total(model):
    s=0
    for i in model.objects.all() :
        s = s+i.montant
    return s
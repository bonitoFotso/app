def total(self):
        s=0
        ss = self.model.objects.all()
        for i in self.model.objects.all() :
            s = s+i.montant
        return s
class Foods:
    def __init__(self, name:str, fc:str, type):
        self.name = name
        self.face = fc
        self.type = type
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Foods('{self.name}', '{self.face}')"
        

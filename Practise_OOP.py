class human:
    
    intelligent=6    #class attributes
    
    def __init__(self, age , gender ):        #constructor.
        self.age= age              #instance attributes
        self.gender=gender
        
    def social_media_WA(self,number):       #class  method with use of self. or is it a instance method???
        self.number=number                  #instance level attributes. doubt is it correct or not # anyways to input number from users??
        print(self.name, "'s number is",self.number)  # any other easy way to print this
        
    
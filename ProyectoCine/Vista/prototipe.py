print("yamete kudasai")


class Sala_cine : #⛀
    # por protocololo y escribo las variables antes
    Id,Nombre,Tipo,Puestos="","","",""
    
    #Declaracion
    def __init__(self,_Id,_Nombre,_tipo,_puestos):
        self.Id=_Id  
        self.Nombre=_Nombre 
        self.Tipo=_tipo 
        self.Puestos=_puestos
        
        
        
    #y si quiero meter otra cosa
    neko2="t"    
    def algo(self,neko1):
        self.neko2=neko1   
    

class Pelicula:  #♦
    
    def __init__(self) -> None:
        self.Titulo
        self.Pais
        self.Director
        self.Actores
        self.Lenguaje
        self.Pais_origen
        self.Sinopsis
        
        #metadato
        self.Caratula
        self.Categoria
        self.Calificacion


class horario():
    
    def __init__(self) -> None:
        self.dia
        self.hora
        



#🃄   	♣ ♦⛀




obj= Sala_cine(1,"sala beta","2d","6")
print(str(obj))
print(obj.Nombre)
obj.algo("algo")
print(obj.neko2) 

#qui dolorem ipsum, quia dolor sit amet consectetur adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam
# on HOLD--------------------
    #id,nombre
Movie= [1,"Pelicula 1" ,"qui dolorem ipsum, quia dolor sit amet consectetur adipisci velit",1 ]
Movie= [1,"Pelicula 1" ,"qui dolorem ipsum, quia dolor sit amet consectetur adipisci velit",2 ] #si la pelicula es de 2 horas toma 2
print( Movie[0]) 

# if tiempo/valor es >1 entonces (t-1) ha que hacer que resta hasta que los tiempo sea 0 y tome la key tupla siguiente y marcarlo como ocupado 

Lunes={7:[],8:"",}
Martes={}

Sala = []

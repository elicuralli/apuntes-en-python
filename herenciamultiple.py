class Telf:
    def __init__(self):
        pass

    def llamar(self):
        print('llamando...')
    
    def ocupado(self):
        print('ocupado...')
    
class Camara:
        def __init__(self):
            pass

        def foto(self):
            print('tomando foto')
    
class Reproduccion:
        def __init__(self):
            pass

        def repro_musica(self):
             print('reproduciendo musica...')
        
        def repro_video(self):
             print('reproduciendo video...')

class smartphone(Telf,Camara,Reproduccion):
     def __del__(self):#elimina las clases no utilizadas de la memoria ejm smartphone ya no es necesaria 
          pass
          #print('telf apagado...')

movil = smartphone()
print(movil.repro_musica())
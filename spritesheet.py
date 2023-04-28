import pygame

class SpriteSheet():
    def __init__ (self,image):
        self.sheet = image 
        
    def Get_Image(self,frame,width,height,scale,color,character):
        image = pygame.Surface((width,height),masks=(color)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width),(character * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image    
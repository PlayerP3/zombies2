import pygame,json
from pygame.math import Vector2
from pynaccle.enemy import Enemy
from pynaccle.moveableobject import Moveable_Object
from pynaccle.utils import *
from pynaccle.objectsystem import objectManager
from pynaccle.weapon import Bullet
from pynaccle.statemachine import StateMachine
from pynaccle.configs import configData
from States.Distraction.death import Death
from States.Distraction.distracting import Distracting
from States.Distraction.thrown import Thrown


# from ItemBench import ItemPools,ItemPoolsReset,remove_from_itempool,add_to_itempool
pygame.font.init()

class Distraction(StateMachine,Bullet):

    def __init__(self):
        
        super().__init__()
        
        self.states = {'THROWN':Thrown(),
                       'DISTRACTING':Distracting(),
                       'DEATH':Death()}
        
        # set parent node for player states
        for x in self.states:
            self.states[x].parent_node = self
        
        self.state = self.states['THROWN']
        
    def init(self):

        set_attributes(game_object=self,attributes=configData.loadedConfigs['throwable'][self.__class__.__name__])

        store_original_vars(game_object=self)
        
        super().init()
        

    
    
    # handle collision damage etc
    def handle_collision(self,game_object:object,axis:str):

        if not self.is_active or not game_object.is_active:
            return

        # set damage variable by checking if there was a crit
        damage = 0
        crit = proc(self.critical_chance)

        if crit:
            damage = self.damage*self.critical_multiplier

        elif not crit:
            damage = self.damage

        # FOR PLAYER BULLETS
        if self.object_of_origin == 'Player':

            # ENEMY OBJECT OF ORIGIN COLLISIONS
            # if projectile is colliding with smth from the enemy or self.object_of_origin == "None"
            if game_object.object_of_origin in ['Enemy','Zombie'] :


                # if it is the boss itself that has been collided with
                if game_object.__class__.__name__ in ["Enemy",'Zombie']:

                    pass
                    # self.apply_damage(gameobj=game_object,damage=damage)
                    

            if game_object.object_of_origin == 'Game':
            
                if game_object.__class__.__name__ == 'Wall':
                    
                    if axis == 'x':
                        if self.movement[0] < 0:
                            self.hurtbox.left = game_object.hurtbox.right

                        elif self.movement[0] > 0:
                            self.hurtbox.right = game_object.hurtbox.left
                            
                        self.movement_vectors['movement']['wall_collisionX'] = True

                    elif axis == 'y':
                        if self.movement[1] < 0:
                            self.hurtbox.top = game_object.hurtbox.bottom

                        if self.movement[1] > 0:
                            self.hurtbox.bottom = game_object.hurtbox.top
                            
                        self.movement_vectors['movement']['wall_collisionY'] = True

            if game_object.object_of_origin == 'Player':
                return
        
    # def update(self):
    
    #         self.state.update()
    
    #         if self.state.done:
    #             self.transition_to_next_state()
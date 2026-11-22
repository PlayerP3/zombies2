import pygame,json
from pygame.math import Vector2
from pynaccle.enemy import Enemy
from pynaccle.utils import *

# from ItemBench import ItemPools,ItemPoolsReset,remove_from_itempool,add_to_itempool
pygame.font.init()

class Zombie(Enemy):

    def __init__(self):

        # movement
        self.movementx = [0,0] # index 0 is no movememnt, -1 left, 1 right
        self.movementy = [0,0] # index 0 is no movement, -1 up, 1 down

        # self.starter_deck = {}
        # self.deck = Deck()

        # target position for shooting
        self.shooting_target_position = (0,0)
        
        super().__init__()

    def select_state(self) -> None:
        
        if self.health <= 0:
            self.state.emit('DEATH')
                    
        # if pathing position exists
        elif self.pathing_end_pos:
            
            # check if we have a target game obejct
            if self.targetGameObject:
                
                # check if we are in range of the target game object
                if find_dist_between_points(self.targetGameObject.hurtbox.center,self.hurtbox.center) <= self.distanceToTriggerAttackState:
                    
                    # if some other thing maybe attack
                    self.state.emit('ATTACKING')
                    
                elif find_dist_between_points(self.targetGameObject.hurtbox.center,self.hurtbox.center) > self.distanceToTriggerAttackState:
                    
                    # if some other thing maybe attack
                    self.state.emit('CHASING')
                    
            # if no target object
            elif not self.targetGameObject:
                
                # # check if we are at the end of the pathing, if not then we leave 
                # if self.current_tile_position != self.pathing_end_pos_tile:
                    
                #     # go to chase
                #     self.state.emit('CHASING')
                self.state.emit('IDLE')
                
        # if no 
                
 
                
                    
class Zombie(Enemy):

    def __init__(self):

        # movement
        self.movementx = [0,0] # index 0 is no movememnt, -1 left, 1 right
        self.movementy = [0,0] # index 0 is no movement, -1 up, 1 down

        # self.starter_deck = {}
        # self.deck = Deck()

        # target position for shooting
        self.shooting_target_position = (0,0)
        
        super().__init__()

    def select_state(self) -> None:
        
        if self.health <= 0:
            self.state.emit('DEATH')
                    
        # if pathing position exists
        elif self.pathing_end_pos:
            
            # check if we have a target game obejct
            if self.targetGameObject:
                
                # check if we are in range of the target game object
                if find_dist_between_points(self.targetGameObject.hurtbox.center,self.hurtbox.center) <= self.distanceToTriggerAttackState:
                    
                    # if some other thing maybe attack
                    self.state.emit('ATTACKING')
                    
                elif find_dist_between_points(self.targetGameObject.hurtbox.center,self.hurtbox.center) > self.distanceToTriggerAttackState:
                    
                    # if some other thing maybe attack
                    self.state.emit('CHASING')
                    
            # if no target object
            elif not self.targetGameObject:
                
                # # check if we are at the end of the pathing, if not then we leave 
                # if self.current_tile_position != self.pathing_end_pos_tile:
                    
                #     # go to chase
                #     self.state.emit('CHASING')
                self.state.emit('IDLE')
                
                
class Shooter(Enemy):

    def __init__(self):

        # movement
        self.movementx = [0,0] # index 0 is no movememnt, -1 left, 1 right
        self.movementy = [0,0] # index 0 is no movement, -1 up, 1 down

        # self.starter_deck = {}
        # self.deck = Deck()

        # target position for shooting
        self.shooting_target_position = (0,0)
        
        super().__init__()

    def select_state(self) -> None:
        
        if self.health <= 0:
            self.state.emit('DEATH')
                    
        # if pathing position exists
        elif self.pathing_end_pos:
            
            # check if we have a target game obejct
            if self.targetGameObject:
                
                # check if we are in range of the target game object
                if find_dist_between_points(self.targetGameObject.hurtbox.center,self.hurtbox.center) <= self.distanceToTriggerAttackState:
                    
                    # if some other thing maybe attack
                    self.state.emit('ATTACKING')
                    
                elif find_dist_between_points(self.targetGameObject.hurtbox.center,self.hurtbox.center) > self.distanceToTriggerAttackState:
                    
                    # if some other thing maybe attack
                    self.state.emit('CHASING')
                    
            # if no target object
            elif not self.targetGameObject:
                
                # # check if we are at the end of the pathing, if not then we leave 
                # if self.current_tile_position != self.pathing_end_pos_tile:
                    
                #     # go to chase
                #     self.state.emit('CHASING')
                self.state.emit('IDLE')
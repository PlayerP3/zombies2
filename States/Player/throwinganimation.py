import pygame,os,re,math,random,string,sys
import json
from pygame.math import Vector2
from pynaccle.statemachine import State
from pynaccle.tilemap import tilemapProcessor


class ThrowingAnimation(State):

    def __init__(self):

        State.__init__(self)
        
        self.throwItem = False
        

    def enter(self):

        self.parent_node.update_direction_vector()
        self.parent_node.movement_vectors['movement']['Xcceleration_rate'] = 0
        self.parent_node.movement_vectors['movement']['acceleration'] = 1


    def update(self):
        
        # run timer
        self.run_timer()
        
        # submit event processing
        self.submit_event_processing()
        
        # run move and collide
        self.parent_node.move_and_collide()

        # update shooting pos
        self.parent_node.update_shooting_target_position()

        # handle stamina
        self.parent_node.update_stamina()

        # movement raycast
        self.parent_node.movement_raycast.init({'starting_position':self.parent_node.hurtbox.center,"target_position":self.parent_node.shooting_target_position})

        # draw surface
        self.parent_node.submit_to_render()

        # self.parent_node.weapon.update()

        self.end_condition()

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            # default player events
            if event.key == pygame.K_a:
                self.parent_node.movementx[0] = -1
                self.parent_node.apply_damage(self.parent_node,0.2)

            if event.key == pygame.K_d:      
                self.parent_node.movementx[1] = 1

            if event.key == pygame.K_w:     
                self.parent_node.movementy[0] = -1

            if event.key == pygame.K_s:
                self.parent_node.movementy[1] = 1   

            # if event.key == pygame.K_e:
            #     self.parent_node.is_interacting = True
    
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                self.parent_node.movementx[0] = 0                

            if event.key == pygame.K_d:
                self.parent_node.movementx[1] = 0
                
            if event.key == pygame.K_w:
                self.parent_node.movementy[0] = 0
            
            if event.key == pygame.K_s:
                self.parent_node.movementy[1] = 0

            # if event.key == pygame.K_e:
            #     self.parent_node.is_interacting = False
            
            if event.key == pygame.K_x:
                self.throwItem = True

    def end_condition(self):
        
        if self.throwItem and self.timer_complete:
            self.emit('THROWITEM')
            
    def completed(self):
        
        self.throwItem = False
        return super().completed()



# has set time to do the throwing animation

# check for key up after animation is done

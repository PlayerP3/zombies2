import pygame,os,re,math,random,string,sys
import json
from pygame.math import Vector2
from pynaccle.statemachine import State
from pynaccle.tilemap import tilemapProcessor
from pynaccle.objectsystem import objectManager


class ThrowItem(State):

    def __init__(self):

        State.__init__(self)

    def enter(self):
        
        # update shooting pos
        self.parent_node.update_shooting_target_position()
        

        # init obj to to be thrown so it getsa thrown immediately
        # get obj
        objToThrow = self.parent_node.inventory.inventory['L2ItemSlot'][0]
        
        # init obj
        objToThrow.init()
        
        # setting start and target pos
        objToThrow.start_position = self.parent_node.hurtbox.center
        objToThrow.hurtbox.center = self.parent_node.hurtbox.center
        objToThrow.target_position = self.parent_node.shooting_target_position

        objToThrow.length_to_target = (Vector2(objToThrow.target_position) - Vector2(objToThrow.hurtbox.center)).length()

        # set bullet direction/current angle
        direction_vectorX, direction_vectorY = Vector2(objToThrow.target_position) - Vector2(objToThrow.start_position)

        # update movement vector
        objToThrow.add_movement_vector(unique_id='movement',direction_vectorX=direction_vectorX,direction_vectorY=direction_vectorY,
                                                    acceleration=objToThrow.acceleration,max_value=0,acceleration_rate_change='negative',
                                                    delete_on_max_value=True)
        # find current angle
        objToThrow.currentAngle = (direction_vectorX,direction_vectorY,0)
        
        objToThrow.is_active = True
        
        objToThrow.pathing = 'regular'
        
        self.parent_node.inventory.inventory['L2ItemSlot'].remove(objToThrow)

        # objToThrow.state = objToThrow.states['THROWN']
        
        objectManager.add_game_object_to_active_pool(objToThrow)
        
        
        # allow movement
        self.parent_node.update_direction_vector()
        self.parent_node.movement_vectors['movement']['acceleration_rate'] = 0
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
        
        self.end_condition()

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            # default player events
            if event.key == pygame.K_a:
                self.parent_node.movementx[0] = -1

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


    def end_condition(self):
        
        if self.timer_complete:
            
            if sum(self.parent_node.movementx) != 0 or sum(self.parent_node.movementy) != 0:
            
                self.emit('WALKING')
            
            self.emit('IDLE')
            
  
    



# has set time to do the throwing animation

# check for key up after animation is done


# throw item
# init the correct object
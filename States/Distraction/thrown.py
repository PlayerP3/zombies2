import pygame,os,re,math,random,string,sys
import json
from pygame.math import Vector2
from pynaccle.statemachine import State
from pynaccle.objectsystem import objectManager
from pynaccle.utils import *

class Thrown(State):

    def __init__(self):

        State.__init__(self)

    def enter(self):

        pass

    def update(self):

        # submit event processing
        self.submit_event_processing()
        
        # movement
        self.parent_node.move_and_collide()
        
        # draw surface
        self.parent_node.submit_to_render()
        
        # update position
        self.parent_node.update_position()
        
        # the state end condition    
        if not self.parent_node.movement_vectors:
            self.emit('DISTRACTING')                   
        
        if self.parent_node.movement_vectors: 
            # update current angle
            self.parent_node.currentAngle = (self.parent_node.movement_vectors['movement']["direction_vectorX"],self.parent_node.movement_vectors['movement']["direction_vectorY"],0)
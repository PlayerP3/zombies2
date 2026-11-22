import pygame,os,re,math,random,string,sys
import json
from pygame.math import Vector2
from pynaccle.statemachine import State
from pynaccle.objectsystem import objectManager
from pynaccle.utils import *

class Death(State):

    def __init__(self):

        State.__init__(self)

    def enter(self):

        pass

    def update(self):
        
        self.run_timer()
        
        # draw surface
        self.parent_node.submit_to_render()
        
        # update position
        self.parent_node.update_position()
        
        if self.timer_complete:
                
            self.parent_node.is_active = False
            self.emit('THROWN')                    
        
                                

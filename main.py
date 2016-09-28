#!/usr/bin/env python2.7

import pygame

import phys_objects
import drawing
import gamestate
from options import Settings
from options import HardSettings
from gamestate import GameStateManager, PlayingState

pygame.init()

settings = Settings()
gamestate_manager = GameStateManager(settings)
playing = PlayingState(settings)
gamestate_manager.set_state(GameStateManager.PLAYING_STATE, playing)

gamestate_manager.set_current_state(GameStateManager.PLAYING_STATE)

size = HardSettings.standard_size()
if settings.dev_mode():
    size = HardSettings.dev_size()
screen = pygame.display.set_mode(size)

still_running = True
clock = pygame.time.Clock()
FPS = HardSettings.fps()

actor = playing.player  # The player's character

while still_running:
    gamestate_manager.pre_event_update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            still_running = False
        else:
            gamestate_manager.handle_event(event)
            
    dt = 1
    gamestate_manager.update(dt)
    gamestate_manager.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

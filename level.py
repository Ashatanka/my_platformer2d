import pygame
from tiles import Tile
from player import Player
from settings import tile_size, screen_width


class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface  # surface is the screen we want the level to display on
        self.setup_level(level_data)  # level_data is level_map from settings
        self.world_shift = 0  # where and how fast to move the camera

    def setup_level(self, layout):

        # the level is a group of tiles and a player
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        # read layout(level_map) and for each X create a tile
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 0.15 * screen_width and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > 0.85 * screen_width and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 5

    # draw the group of tiles we created in def setup_level
    def run(self):

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # player
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()
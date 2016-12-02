def __init__(self, width, height):
    super().__init__(width, height)
 
    arcade.set_background_color(arcade.color.BLACK)
 
    self.ship = arcade.Sprite('images/ship.png')
    self.ship.set_position(100, 100)
    
def on_draw(self):
    arcade.start_render()
 
    self.ship.draw()

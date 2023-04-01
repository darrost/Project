class Settings:

    def __init__(self):
        self.screen_width = 2560
        self.screen_height = 1440
        self.bg_color = (10, 10, 30)
         
        self.ship_speed = 15

        self.ship_limit = 3
        
        self.bullet_speed = 60
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (10, 180, 180)
        self.bullets_allowed = 6

  
        self.fleet_drop_speed = 30
        self.fleet_direction = 4

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed = 5.0
        self.fleet_direction = 1

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale    
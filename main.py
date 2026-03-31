class TemperatureController:
    def __init__(self, target_temp, min_temp=0, max_temp=100):
        self.target_temp = target_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.current_temp = 20
    
    def heat(self, amount):
        """Increase temperature"""
        self.current_temp = min(self.current_temp + amount, self.max_temp)
    
    def cool(self, amount):
        """Decrease temperature"""
        self.current_temp = max(self.current_temp - amount, self.min_temp)
    
    def adjust(self):
        """Automatically adjust to reach target temperature"""
        if self.current_temp < self.target_temp:
            self.heat(1)
        elif self.current_temp > self.target_temp:
            self.cool(1)
    
    def get_status(self):
        """Return current status"""
        return {
            'current': self.current_temp,
            'target': self.target_temp,
            'status': 'OK' if self.current_temp == self.target_temp else 'Adjusting'
        }


if __name__ == "__main__":
    controller = TemperatureController(target_temp=50)
    for _ in range(40):
        controller.adjust()
    print(controller.get_status())
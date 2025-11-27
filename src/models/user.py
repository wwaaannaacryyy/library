class User:
    def __init__(self, name: str, role: str, tel: int):
        self.name = name
        self.role = role
        self.tel = tel
    def __str__(self):
      return f"Имя - {self.name}, Роль - {self.role}, Телефон - {self.tel}" 
    
        
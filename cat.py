
class Cat:
    def __init__(self , name , age ):
        self.name = name ,
        self.age = age ,
        self.emotional_health = 100 ,
        self.is_alive = True ,
        self.legs = 4 ,

    def get_info_about_cat (self):
        print(f"[CAT_NAME] : {self.name}")
        print(f"[CAT_AGE] : {self.age}")
        print(f"[CAT_EH] : {self.emotional_health}")
        print(f"[CAT_IS_ALIVE] : {self.is_alive}")
        print(f"[CAT_LEGS_COUNT] : {self.legs}")

    def got_bad_news (self , howMuch ) :
        self.emotional_health = howMuch
        print(f"Cat already has a bad news, crying over, now EH is equal: {self.emotional_health}")

    def drinks_milk (self , howMuch) :
        self.emotional_health = howMuch
        print(f"Cat already has a bad news, crying over, now EH is equal: {self.emotional_health}")



katty = Cat(name= "Katty" , age=13)

katty.get_info_about_cat()

news = input("U'll haven't some cat-drags [ENTER-DAMAGE FOR CAT]: ")

katty.got_bad_news(int(news))

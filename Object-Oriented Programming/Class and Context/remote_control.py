class RemoteControl:

    def __init__(self, tv, room):
        self.tv = tv
        self.room = room


    def next_channel(self):
        print('Next channel')

    def back_channel(self):
        print('Back channel')
    
    def change_channel(self, channel):
        print("Change channel to: {}".format(channel))


controler_living_room = RemoteControl('LG', 'Living Room')
print(controler_living_room.room)
print(controler_living_room.tv)
controler_living_room.next_channel()
controler_living_room.change_channel(12)

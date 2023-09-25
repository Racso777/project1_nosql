import redis
import json
import threading
import random
import sys

class Chatbot:
    def __init__(self, host='redis', port=6379):
        self.client = redis.StrictRedis(host=host, port=port)
        self.pubsub = self.client.pubsub()
        self.username = None

    def introduce(self):
        # Provide an introduction and list of commands
        # TASK 2
        intro = """
        Hello I'm your friendly Redis chatbot.
        Here are the commands you can use:
        !help: List of commands
        !weather <city>: Weather update
        !fact: Random fun fact
        !whoami: Your user information
        """
        print(intro)

    def identify(self, username, age, gender, location):
        #TASK 3
        # Store user details in Redis
        hash_key = username

        # Define the field-value pairs to set
        field_value_pairs = {
            'age': age,
            'gender': gender,
            'location': location,
        }

        # set the username to current name
        self.username = username
        #self.client.hmset(hash_key, field_value_pairs)
        # Use hmset to set multiple field-value pairs in the hash
        for field, value in field_value_pairs.items():
            self.client.hset(hash_key, field, value)

    # TASK 4
    def join_channel(self, channel):
        # Join a channel
        self.pubsub.subscribe(channel)

    def leave_channel(self, channel):
        # Leave a channel
        self.pubsub.unsubscribe(channel)

    def send_message(self, channel, message):
        # Send a message to a channel
        output_message = {
            "username": self.username,
            "message": message
        }
        message_str = json.dumps(output_message)
        self.client.publish(channel, message_str)

    def read_message(self, channel):
        # Listen for messages on the subscribed channels
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                # Process the received message
                channel = message['channel'].decode('utf-8')
                data = message['data'].decode('utf-8')
                print("")
                print(f"Message from channel '{channel}': {data}")

    # TASK 5
    def process_commands(self):    
        # Define a dictionary of fun facts
        fun_facts = [
            "The Eiffel Tower can be 15 cm taller during the summer due to the expansion of the iron.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "A group of flamingos is called a 'flamboyance.'",
            "The world's largest desert is not the Sahara but Antarctica.",
            "Bananas are berries, but strawberries are not.",
            "Octopuses have three hearts: two pump blood to the gills, and one pumps it to the rest of the body.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes.",
            "The average person spends six months of their life waiting for red lights to turn green."
        ]

        # Define a dictonary for weather city data
        weather_data = {
            "New York": {
                "temperature": 25.0,  
                "description": "Partly cloudy",
                "humidity": 45,       
                "pressure": 1013     
            },
            "Los Angeles": {
                "temperature": 28.5,
                "description": "Sunny",
                "humidity": 60,
                "pressure": 1015
            },
            "London": {
                "temperature": 18.2,
                "description": "Overcast",
                "humidity": 75,
                "pressure": 1011
            },
            "Paris": {
                "temperature": 22.8,
                "description": "Partly cloudy",
                "humidity": 50,
                "pressure": 1014
            },
            "Tokyo": {
                "temperature": 30.7,
                "description": "Clear sky",
                "humidity": 55,
                "pressure": 1010
            }
        }


        if user_input == "!help":
            print("Available commands:")
            print("!help: List of commands")
            print("!weather <city>: Weather update (Capitalize First letter for City Name)")
            print("!fact: Random fun fact")
            print("!whoami: Your user information")
            print("!exit: Exit the program")
    
        elif user_input.startswith("!weather"):
            # Extract the city from the input
            test = user_input.split()
            if len(test) > 1:
                city = user_input.split(" ", 1)[1]
                print(f"Getting weather update for {city}...")
            else:
                city = ""
                
            # weather retrieval logic
            if city in weather_data:
                city_weather = weather_data[city]
                print(f"Weather in {city}:")
                print(f"Temperature: {city_weather['temperature']}°C")
                print(f"Description: {city_weather['description']}")
                print(f"Humidity: {city_weather['humidity']}%")
                print(f"Pressure: {city_weather['pressure']} hPa")
            else:
                print(f"Weather data for {city} not found.")
    
        elif user_input == "!fact":
            random_fact = random.choice(fun_facts)
            print(f"Fun Fact: {random_fact}")
    
        elif user_input == "!whoami":
            if self.username == None:
                print("You need to identify yourself first.")
            else:
                print(f"Hello, {self.username}! You are the user.")
            
        else:
            print("Invalid command. Type !help for a list of commands.")

    def get_user_info(self,username):
        # Get the user info that the user set
        # Define the key of the hash
        hash_key = username

        list = self.client.hgetall(hash_key)
        # Create an empty dictionary to store the string values
        string_dict = {}
        
        # Convert bytes to strings and store them in the new dictionary
        for key, value in list.items():
            string_key = key.decode('utf-8')
            string_value = value.decode('utf-8')  # Use the appropriate encoding
            string_dict[string_key] = string_value
        
        # Print the resulting dictionary of strings
        print(string_dict)

if __name__ == "__main__":
    # set up a chatbot object
    bot = Chatbot()
    bot.introduce()

    # main loop
    while True:
        user_input = input("""
Options: 
1. Identify yourself
2. Join a channel
3. Leave a channel
4. Send a message to a channel
5. Get info about a user
6. Exit
!help: List of commands
!weather <city>: Weather update
!fact: Random fun fact
!whoami: Your user information
Enter Your Choice: """
        )
        
        #different logic for different choice
        if user_input == "1":
            username = input("Enter your username: ")
            age = input("Enter your age: ")
            gender = input("Enter your gender: ")
            location = input("Enter your location: ")
            bot.identify(username,age,gender,location)
            print(f"Hello, {username}! You have been identified.")

        elif user_input == "2":
            channel = input("Enter the channel name that you want to join: ")
            bot.join_channel(channel)
            print(f"Listening to: '{channel}'")
            # Create a thread for the subscription process
            subscription_thread = threading.Thread(target=bot.read_message, args=(channel,))
            
            # Start the subscription thread
            subscription_thread.start()

        elif user_input == "3":
            channel = input("Enter the channel name that you want to leave: ")
            bot.leave_channel(channel)
            print(f"You are out of the channel: '{channel}'")

        elif user_input == "4":
            channel = input("Enter channel name: ")
            message = input("Enter your message: ")
            bot.send_message(channel, message)

        elif user_input == "5":
            user = input("Enter the user you want to know: ")
            bot.get_user_info(user)

        elif user_input == "6":
            print("Good Bye!")
            sys.exit()

        else:
            bot.process_commands()
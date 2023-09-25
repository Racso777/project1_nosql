# project1_nosql
This is a simple chatbot using Redis's Pub/Sub mechanism.
It allows you to identify as an user and listen to different channel in redis database and receive message from other users in real time.
Here's are how to use this chatbot:
You can run the chatbot by running this command in the command line prompt
You can identify yourself by typing 1 and input your name and information
<img width="531" alt="截屏2023-09-25 下午3 08 07" src="https://github.com/Racso777/project1_nosql/assets/111296013/ebc2803d-90f3-4d9d-8e53-de6bf12eb2b3">

You can listen to a specific channel by typing 2 and input channel name
<img width="531" alt="截屏2023-09-25 下午3 08 20" src="https://github.com/Racso777/project1_nosql/assets/111296013/6ffae710-766d-4c35-a171-7c71044f3c5a">

You can leave a specific channel by typing 3 and input channel name
<img width="536" alt="截屏2023-09-25 下午3 08 32" src="https://github.com/Racso777/project1_nosql/assets/111296013/85ac80a1-ba5e-400a-8a81-f822c1b0e10c">

You can send a specific message to a specific channel by typing 4 and input channel name and message
<img width="536" alt="截屏2023-09-25 下午3 08 32" src="https://github.com/Racso777/project1_nosql/assets/111296013/58bd25b4-b272-4e78-bb44-85a69106ad34">

If someone is listening to that channel (including yourself) will receive that message immediately 
<img width="535" alt="截屏2023-09-25 下午3 08 49" src="https://github.com/Racso777/project1_nosql/assets/111296013/8c7a9770-be61-4a0e-aeb5-5ab0bd0cc14d">

You can find the information about an user by typing 5 and input their name
<img width="541" alt="截屏2023-09-25 下午3 09 10" src="https://github.com/Racso777/project1_nosql/assets/111296013/cc7b830a-0a11-4bbf-ba59-16b3ab0be6bd">

You can type in !help for help with command you can use

You can type in !weather <city> to see the weather data for that city, you will need to capitalize the first letter of the city name

You can type in !fact for a random fun fact

You can type in !whoami to look for your own information

if you didn't identify yourself first, you will not get information for typing !whoami

You

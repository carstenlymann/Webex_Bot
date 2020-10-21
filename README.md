# Webex_Bot

### Installation

1. Clone the repo
```sh
git clone https://github.com/carstenlymann/Webex_Bot.git
```

2. Install requirements.txt
```sh
pip3 install -r requirements.txt
```

3. Find your Webex Bearer Token and the Webex Room id where you want to receive these messages
```sh
Bearer Token can be found here: https://developer.webex.com/docs/api/getting-started

I used Postman to find my room id
In postman:
	1. Get request to: https://webexapis.com/v1/rooms
	2. Under Authorization enter your Bearer Token
	3. Send
	4. Click the Body tab and find your Room id and title
	5. Copy those to the script



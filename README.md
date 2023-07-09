# Twitch_title_to_telegram_bot
Twitch title to Telegram
Script gets title from Twtich.tv API and send it to Telegram bot. Without chat commands starting with "!". For example: !discord 

How to get client id and access token from Twitch:
    
    - Go to the Twitch Application Management page and sign in to your Twitch account.

    - Click on "Create Application". Fill out the form with your application name, OAuth Redirect URLs (you can use 'http://localhost'), and select an application category. Accept the terms of service and click "Create".

    - After creating the application, you will see the 'client-id' on your application page.

    - To obtain the 'access-token', you need to make an OAuth request (Follow the link). You can do this by visiting the following URL, replacing 'client-id' and 'redirect-uri' with the values from your application:

    https://id.twitch.tv/oauth2/authorize?client_id=HERE_YOUR_CLIENT_ID&redirect_uri=HERE_YOUR_REDIRECT_URI&response_type=token

    - After clicking on the link, you will receive your access token in the URL:

    http://localhost/#access_token=HERE_YOUR_ACCESS_TOKEN&scope=&token_type=bearer

How to create a Telegram bot and get your bot token:
    
    - Open @BotFather in Telegram.

    - Send the command /newbot and create a title that ends with "bot". For example: shroud_title_bot.

How to get your chat id in Telegram

    - Go to @get_my_telegram_chat_id_bot click on Start and get your chat id

After you have obtained all the necessary authorization data, specify them in the config.ini file (without quotation marks).

The program is ready to run.

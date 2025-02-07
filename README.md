Twitter bot that will create images when you tag him and say "Draw me".
To use it:
    1. Create a twitter developer account and create you app, make sure to add the read and write setting for the keys before you generate them.
    2. Change the credentials of config.yaml with you twitter keys and openain keys.
       Take into account twitter will allow you to retreive twits once every 12 mins.  
    3. Also on the yaml change the name of the project to the one you want and the username to the one of the twitter account you will be using. 
    4. launch the bot, for that is recomended to create a virtual enviroment.
    5. pip install -r requirements.txt
    6. Run twitter_bot.py and  the bot should be running. 
    7. Tag the account from other account on twitter and say "draw me" and check the result.
    8. play with the prompt generator of the image on image_generator.py to change the results of the images and the styles.

.
    Thanks for reading.

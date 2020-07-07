# Image Collector Telegram Bot

If we want to have a great result from Machine Leaning Algorithms, we should provide them a lot fuel for them.
**Data is Fuel.** 

In this repository, a telegram bot is implemented to collect data which is people's selfie photo and national photo to use in _Face Verification_ problem.

If you want to see how this bot works please start https://telegram.me/face_image_collector_bot.
## How to run this bot?

### using Docker 
In first step, build your docker image:
    ``` docker build -t image_collector_bot .```

Then run the docker image:
    ``` docker run image_collector_bot```

### In local
1. Set SIMPLE-SETTING environment variable:
    
    ```export SIMPLE_SETTINGS=settings```
    
2. Run the code. 

    ```python image_collector_bot.py```


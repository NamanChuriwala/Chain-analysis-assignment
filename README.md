## Prerequisites
1. We have tested the application on Debian 10 and Python 3.7. We recommend you to run the app on a Linux distribution only.

## Steps to Build
1. `git clone https://github.com/NamanChuriwala/Chain-analysis-assignment.git`
2. `cd Chain-analysis-assignment`
3. `pip install -r requirements.txt`

## Steps to Run
1. `$> python app.py`
2. `Go to 0.0.0.0:5000/prices`

## Live version
1. The live version can be found at https://emerald-result-329102.uc.r.appspot.com/prices/

## Questionnaire:

1. Are there any sub-optimal choices( or short cuts taken due to limited time ) in your implementation?
    I have not stuck to the Object Oriented way of design in this implementation due to lack of time. Also I have
    not spent a lot of effort in improving the Frontend of the webpage, which could have been improved.
    
2. Is any part of it over-designed? ( It is fine to over-design to showcase your skills as long as you are clear about it)
    No. The implementation is kept very simple.
    
3. If you have to scale your solution to 100 users/second traffic what changes would you make, if any?
    Since Flask is supposed to be used for development and not production, I would use a WSGI to talk to a reverse proxy or load
    balance such as NGINX to be able to handle concurrent requests. Also, I have deployed the webpage using serverless on Google Cloud
    which automatically scales horizontally (adds servers upon increased load), which should take care of horizontal scaling.
    
4. What are some other enhancements you would have made, if you had more time to do this implementation
    I would have used a more appropriate framework for the task such as Django, and spent more time on the frotnend by incorporating
    some CSS. Also, would have handled secret keys more efficiently (Right now the API keys I have generated are disabled for transactions, 
    which might not be true for enterprise applications)

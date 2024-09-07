# A SIMPLE DYNAMIC PORTFORLIO PROJECT FOR BEGINNERS
this project is dedicated to all newbies in the industry who want to learn by doing real life project. I have a dedicated Youtube video where all the steps followed in the development of this project is hosted please feel free to get in touch with me on youtube at https://www.youtube.com/@learnpro_ng/videos 

# instructions on how to install and run the script
1. install the required libraries by running the following command in your terminal
python -m venv myenv
myenv\Scripts\activate for windows 
myenv\bin\activate for mac/linux

then install django

after activating the virtual environment go ahead to install the requirements.txt file using this command
pip install -r requirements.txt
then run the migrations
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
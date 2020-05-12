# Epg_API


This Project by KavehRS is licensed under a

<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">Creative Commons 
Attribution Non-Commercial 3.0 License</a>.


Installation Guide:

1- Create virtual environment:

    virtualenv epg-env
    
2- Activate virtual environment:

    .\epg-env\scripts\activate
    
3- Install requirements:

    pip install -r requirements.txt
    
4- Apply migrations:

    python manage.py migrate
    
5- Start project on desired port:

    python manage.py runserver 8000
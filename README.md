# How to integrate Django into your React project.

## Introduction

In this article, we will demonstrate how to integrate python's Django framework into a reactjs Project. First, let us look at what React and Django mean

## React

React or Reactjs refers to a [Javascript](https://www.freecodecamp.org/news/what-is-javascript-definition-of-js/#:~:text=JavaScript%20is%20a%20dynamic%20programming,with%20only%20HTML%20and%20CSS.) library that is used to build interactive elements in web development. That means it is used by developers to build user interfaces(UI). React also has solid documentation that you can explore through this [link](https://reactjs.org/docs/getting-started.html) and a vibrant ecosystem around it.

## Django

Django refers to a high-level, free, and open-source Python web framework capable of the rapid development of secure and maintainable websites. It solves much of web development hassles so that a developer can focus on writing their app without the need to reinvent the wheel. It also has extensive documentation that you can use to explore its functionalities. You can check for further knowledge of Django though [here](https://docs.djangoproject.com/en/4.1/).

## Source Code

Get the GitHub source code [here](https://github.com/apeli23/reactdjango.git)

## Prerequisites

This article requires a prior entry-level understanding of javascript, react, and python language.
Install the following applications. Click on any of them to be redirected to its installation guide: [python](https://www.python.org/downloads/) [django](https://docs.djangoproject.com/en/4.1/intro/install/) [nodejs](https://nodejs.org/en/download/) and [vscode](https://code.visualstudio.com/download)(or your preferred code editor).

**_ This article will be based on the Linux os terminal_**

## Sample Project Setup

Create a folder to contain your project. Let us name it `reactdjango`. Inside it, create a new react app using the following command

```
"Terminal"

npx create-react-app react
```

The command above will create a new folder named `react` and inside it, we will store the files required to run a react application. In your terminal, head to the project directory and use the following command to run your application

```
"Terminal"

npm start
```

The command above will run the project on the local host of your pc. In the terminal, you will be offered a link that looks like `http://localhost:3000` which on clicking will direct you to a webpage that looks like follows

![create-react-app](https://res.cloudinary.com/dlt0f5pvq/image/upload/v1670588076/Screenshot_7_a7uacw.png 'create-react-app')

With the above UI, we have successfully configured a functioning react project for the front end.

Head back to your project root directory. We assume you have [`Django installed](https://docs.djangoproject.com/en/4.1/intro/install/) already.
Create a new Django project using the following command,

```
"react terminal"

Django-admin startproject django
```

To integrate Django into the react project, cut the `react` folder and paste it into the `django` folder you just created then run the following command in your react terminal.

```
"react terminal"

npm run build
```

The command above will create the `build` folder in the react root directory. We will use the `build/index.html` directory to integrate the Django template.
Head to the `backend/settings.py` directory and start by including the following import

```
"backend/settings.py"

import os
```

Edit the `TEMPLATE` property to include the `index.js` file in the build folder.

```
"backend/settings.py"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'reactdj/build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

In Django, there are the template files that we configure for the web pages and also the static files which involve any external files used in our templates e.g images, css, or css files. Therefore we configure the location of the static files by adding the following code in the `backend/settings.py` directory below the `STATIC_URL` property.

```
"backend/settings.py"

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'reactdj/build/static')
    ]
```

The code above will inform Django that the static files will be in the `backend/reactdj/build/static` directory.
To complete the static files configuration procedure, we need to involve URL mapping.
Create a new file inside the backend folder called `views.py` and paste the following code

```
"backend/views.py"

from django.shortcuts import render; #allows Django to render a template file

def index(request):
    return render(request, 'index.html')

```

The code above will look to render `index.html` file. We have to involve the file above to `urls.py`. Head to `backend/urls.py` directory and replace its contents with the following.
;

```
"backend/urls.py`"

from django.contrib import admin
from django.urls import path
from . import views;



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]

```

In the code above, we have created a URL path for the `views` file.
Now we are ready to run the Django project on the localhost. Use the following command in the backend terminal

```
"backend terminal"

python manage.py runserver
```

Django will provide a link that looks like `http://127.0.0.1:8000/`. If you run the link in your browser, It will provide a react frontend UI, which confirms react integration with Django.
Currently, we only have the default react template. Feel free to clone the [github](https://github.com/apeli23/reactdjango.git) repo and make changes as you see fit. React and Django integration chive an easy way to manage code for both the backend and front end since the front end and backend are separately written in Django hence making testing, finding, and removing bugs easier.

Happy coding!

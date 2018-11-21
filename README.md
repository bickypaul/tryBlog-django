# tryBlog-django
A simple  django based Blog WebApp with authentication and other features.

Do check out the screenshots first.

This webapp basically allows a user to post a blog of their own. They can also check out other blogs posted by other users.
User has to sign up first and then login to post a blog, update a blog and delete a blog.
User can update their username, email id and change their profile picture as well.

# Requirements (Tested on)
# 1. Ubuntu 18.04
# 2. Python 3
# 3. django 2.1.2

# How to execute it to run on your local machine.
# 1. git clone https://github.com/bickypaul/tryBlog-django/
# 2. cd tryBlog-Django
# 3. python3 manage.py makemigrations
# 4. python3 manage.py migrate
# 5. python3 manage.py runserver
# 6. Goto http://localhost:8000

# Authentication Views
Django Authentication Views has been integrated in this project. for example:
# 1. LoginView
# 2. LogoutView
# 3. PasswordResetView
# 4. PasswordResetDoneView
# 5. PasswodResetConfirmView
# 6. PasswordResetCompleteView

# BlogPost Views
Django generic views has been used to render templates for certain blogpost actions like:
# 1. ListView
# 2. DetailView
# 3. CreateView
# 4. UpdateView
# 5. DeleteView

# django built-in decorators
# 1. login_required
# 2. reciever 

# django signals
django signals to fire a function after a certain action has been performed like:
# 1. post_save

# django built-in 
Mixins for the class based views to check authenticated routes and permissions to perform certain actions like:
# 1. LoginRequiredixin
# 2. UserPassesTestMixin

# All in all, this sole purpose of mine behind developing this project (webapp) was to further my coding skills in python/django and significant understanding of the django web development framework. Although, it couldn't have been possible without some youtube tutorials on django and the awesome django documentation provided by the django community. Also how can I forget Stackoverflow.com 

Do checkout the screenshots of the project and the project as well. Thank you for reading. 


from django.conf.urls import patterns, include, url


urlpatterns = [
                url(r'^hello/','simpleapp.views.hello',name = 'hello'),
                url(r'^addUser/','simpleapp.views.saveUser', name = 'saveNewUser')
            ]

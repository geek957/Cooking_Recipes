# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Learn',SPAN(2),'COOK'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="#",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index') ),
    (T('My Recipies'),False,URL('default','My_Recipies')),
    (T('share your Recipie'), False, URL('default', 'upload_your_recipie') ),
    (T('Edit/Delete Your uploads'),False, URL('default', 'test')),
    (T('List of all Users'),False,URL('default','userlist')),
    (T('Your Profile'),False,URL('default','viewprofile')),
    (T('search Recipes'),False,URL('default','search'))
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
          (T('For More!!'), False, None, [
             (T('youtube'), False,
              'https://www.youtube.com/user/Manjulaskitchen'),
              (T('Twitter'), False, 'https://twitter.com/recipes'),
              (T('Live Chat'), False,
               'food.ndtv.com'),
              ]),
        ]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()

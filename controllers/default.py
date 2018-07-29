# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
@auth.requires_login()

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Ready to Taste")
    message=T('Welcome to the Food World!!')
    if not request.vars.page:
        redirect(URL(vars={'page' : 1}))
    else :
        page=int(request.vars.page)
        start=(page-1)*10
        end=page*10
        r=db(db.Reciepe_post).count()
        int(r)
        if(r%10==0):
            r=r/10
        else:
            r=r/10 + 1
        posts=db(db.Reciepe_post).select(orderby=~db.Reciepe_post.created_on,limitby=(start,end))

    return locals()
def index1():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Ready to Taste")
    message=T('Welcome to the Food World!!')
    if not request.vars.page:
        redirect(URL(vars={'page' : 1}))
    else :
        page=int(request.vars.page)
        start=(page-1)*10
        end=page*10
        r=db(db.Reciepe_post).count()
        int(r)
        if(r%10==0):
            r=r/10
        else:
            r=r/10 + 1
        posts=db(db.Reciepe_post).select(orderby=~db.Reciepe_post.votes,limitby=(start,end))

    return locals()
@auth.requires_login()
def Details():
    ide=request.args(0,cast=int)
    post = db.Reciepe_post(ide)
    comments=db(db.images.Recipe_id==ide).select()
    return locals()
@auth.requires_login()
def userlist():
    if not request.vars.page:
        redirect(URL(vars={'page' : 1}))
    else :
        page=int(request.vars.page)
        start=(page-1)*10
        end=page*10
        r=db(db.auth_user).count()
        int(r)
        if(r%10==0):
            r=r/10
        else:
            r=r/10 + 1
    posts=db(db.auth_user).select(limitby=(start,end))
    return locals()

def userprofile():
    post = db.auth_user(request.args(0,cast=int))
    return locals()

def useruploads():
    ide=request.args(0,cast=int)
    name=db.auth_user(ide).first_name
    posts=db(db.Reciepe_post.iden==ide).select(orderby=~db.Reciepe_post.votes)
    
    return locals()
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

def edit_post():
    id=request.args(0,cast=int)
    form=SQLFORM(db.Reciepe_post, id).process(next='Details/[id]')
    return locals()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
@auth.requires_login()

def upload_your_recipie():
    db.Reciepe_post.Name.default=auth.user.first_name
    db.Reciepe_post.Name.writable=False
    db.Reciepe_post.Name.readable=False
    db.Reciepe_post.iden.default=auth.user.id
    db.Reciepe_post.iden.writable=False
    db.Reciepe_post.iden.readable=False
    form=SQLFORM(db.Reciepe_post)
    if form.accepts(request,session):
        redirect(URL('My_Recipies'))
    return locals()
@auth.requires_login()

def My_Recipies():
    rows=db(db.Reciepe_post.iden==auth.user.id).select()
    if not request.vars.page:
        redirect(URL(vars={'page' : 1}))
    else :
        page=int(request.vars.page)
        start=(page-1)*10
        end=page*10
        r=db(db.Reciepe_post).count()
        int(r)
        if(r%10==0):
            r=r/10
        else:
            r=r/10 + 1
        posts=db(db.Reciepe_post.iden==auth.user.id).select(orderby=~db.Reciepe_post.created_on,limitby=(start,end))
    return locals()
@auth.requires_login()
def test():
    query=((db.Reciepe_post.iden==auth.user.id))
    rows=SQLFORM.grid(query=query)
    return locals()
@auth.requires_login()
def viewprofile():
    iden= auth.user.id
    post = db.auth_user(iden)
    return locals()

@auth.requires_login()
def editimages():
    ide=request.args(0,cast=int)
    query=((db.images.Recipe_id==ide))
    col=SQLFORM.grid(query=query)
    return locals()

def addimage():
    id=request.args(0,cast=int)
    db.images.Recipe_id.default=id
    db.images.Recipe_id.readable=False
    db.images.Recipe_id.writable=False
    form=SQLFORM(db.images)
    if form.accepts(request,session):
        redirect(URL('My_Recipies'))
    return locals()

def posts():
    if not request.vars.page:
        redirect(URL(vars={'page' : 1}))
    else :
        page=int(request.vars.page)
        start=(page-1)*10
        end=page*10
        posts=db(db.Reciepe_post).select(orderby=~db.Reciepe_post.created_on,limitby=(start,end))
        return dict(posts=posts)

def likes():
    vars = request.post_vars
    if vars and auth.user:
        id = vars.id
        direction = +1 if vars.direction == 'up' else -1
        post = db.Reciepe_post(id)
        if post:
            vote = db.vote(post=id,created_by=auth.user.id)
            if not vote:
                if direction==1 :
                    post.update_record(votes=post.votes+direction)
                    db.vote.insert(post=id,score=direction)
                else:
                    pass
            elif vote.score!=direction:
                post.update_record(votes=post.votes+direction)
                vote.update_record(score=direction)
            else:
                pass
    """
    if vars:
        id=vars.id
        direction=+1 if vars.direction=='up' else -1
        post=db.Reciepe_post(id)
        if post:
            post.update_record(votes=post.votes+direction)
    """
    return str(post.votes)
def search():
    """an ajax wiki search page"""
    return dict(form=FORM(INPUT(_id='keyword',_name='keyword',
_onkeyup="ajax('callback', ['keyword'], 'target');")),
target_div=DIV(_id='target'))

def callback():
    """an ajax callback that returns a <ul> of links to wiki pages"""
    query = db.Reciepe_post.Title.contains(request.vars.keyword)
    pages = db(query).select(orderby=db.Reciepe_post.Title)
    links = [A(p.Title, _href=URL('Details',args=p.id)) for p in pages]
    return UL(*links)

@auth.requires_membership("admin")
def admini():
    dict(message=T('Welcome Admin!!'))
    posts=SQLFORM.smartgrid(db.auth_user, linked_tables=['Reciepe_post'])
    return locals()

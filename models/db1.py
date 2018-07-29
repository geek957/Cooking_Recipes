# -*- coding: utf-8 -*-


db.define_table('Reciepe_post',
                Field('Title',unique=True,requires=IS_NOT_EMPTY()),
                Field('Description','text',requires=IS_NOT_EMPTY()),
                Field('Serves','integer',requires=IS_NOT_EMPTY()),
                Field('Prep_time','time',requires=IS_TIME()),
                Field('Cook_time','time',requires=IS_TIME()),
                Field('Ingredients','text',requires=IS_NOT_EMPTY()),
                Field('Instructions','text',requires=IS_NOT_EMPTY()),
                Field('Notes','text',requires=IS_NOT_EMPTY()),
                Field('Image','upload',requires=IS_IMAGE()),
                Field('Name',readable=False,writable=False),
                Field('iden',readable=False,writable=False),
                Field('votes','integer',default=0,readable=False,writable=False),
                auth.signature)
db.define_table('vote',
               Field('post' ,'reference Reciepe_post'),
               Field('score','integer',default=+1),
               auth.signature)


db.define_table('images',
               Field('Recipe_id','reference Reciepe_post'),
               Field('Add_Image','upload',requires=IS_IMAGE()))

db.images.Recipe_id.requires=IS_IN_DB(db,db.Reciepe_post.id, '%(title)s')

from xmlrpc import client

url='https://dgaribayghcrucialsoft-crucialsoftcurso-main-v2-0-2929627.dev.odoo.com'
db='dgaribayghcrucialsoft-crucialsoftcurso-main-v2-0-2929627'
username='dgaribay@crucialsoft.com.mx'
password='q1w2e3r4'

common=client.ServerProxy("{}/xmlrpc/2/common".format(url))
print('version = ')
print(common.version())

uid=common.authenticate(db,username,password,{})
print('uid = ',uid)

models=client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access=models.execute_kw(db, uid, password,
                               'academy.session', 'check_access_rights',
                               ['write'], {'raise_exception': False})
print('model_access = ',model_access)

courses=models.execute_kw(db, uid, password,
                          'academy.course', 'search_read',
                          [[['level','in', ['intermediate','beginner']]]])
print('Cursos=')
print(courses)

course=models.execute_kw(db, uid, password,
                         'academy.course', 'search',
                         [[['name','=', 'Química III']]])
print('ID del Curso Química III = ',course)

session_fields=models.execute_kw(db, uid, password,
                                 'academy.session', 'fields_get',
                                 [], {'attributes':['string','type','required']})
print('Campos de la sesión = ')
print(session_fields)

new_session=models.execute(db, uid, password,
                           'academy.session','create',
                           [
                               {
                                   'course_id': course[0],
                                   'state':'open',
                                   'duration': 5,
                                   
                               }
                           ])
print('ID de la nueva sesión = ',new_session)
import random
import string
from model.project import Project



def random_name(prefix, maxlen):
    symbols = string.ascii_letters+string.digits + string.punctuation + " "
    return prefix + "".join((random.choice(symbols) for i in range(random.randrange(maxlen))))

def random_desk(prefix, maxlen):
    symbols = string.ascii_letters+string.digits + string.punctuation + " "*20
    return prefix + "".join((random.choice(symbols) for i in range(random.randrange(maxlen))))

def test_create_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    project = Project(name=random_name("Name", 10), description=random_desk("Desc", 100))
    app.project.add_project(project.name, project.description)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

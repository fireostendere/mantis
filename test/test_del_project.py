from model.project import Project
import random



def test_delete_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    if len(app.soap.get_project_list(username, password)) == 0:
        app.project.create(Project(name="NewName", description="NewDesc"))
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
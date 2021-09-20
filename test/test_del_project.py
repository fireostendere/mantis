from model.project import Project
import random



def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="NewName", description="NewDesc"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
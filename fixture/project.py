from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self, name, description):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td/form/input[2]").click()
        self.fill_project_form(name, description)
        wd.find_element_by_class_name("button").click()

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, name, description):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(description)


    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        self.project_cache = []
        for element in wd.find_elements_by_xpath("//td/a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
            text = element.text
            id = element.get_attribute("href").replace(
                self.app.base_url + '/manage_proj_edit_page.php?project_id=',
                ''
            )
            self.project_cache.append(Project(name=text, id=id))
        return list(self.project_cache)

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_id(id)
        wd.implicitly_wait(0.1)
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()


    def select_project_by_id(self, id):
        wd = self.app.wd
        id = str(id)
        wd.get(self.app.base_url + "/manage_proj_edit_page.php?project_id="+id)
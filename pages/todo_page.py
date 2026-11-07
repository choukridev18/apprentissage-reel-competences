from playwright.sync_api import Page


class TodoPage:

    URL = "https://demo.playwright.dev/todomvc"

    def __init__(self, page: Page):
        self.page = page
        self.champs = self.page.get_by_placeholder("What needs to be done?")

    def navigate(self):
        self.page.goto(self.URL)

    def fill_field_todo_and_submit(self, tache):
        self.champs.fill(tache)
        self.champs.press("Enter")

    def find_todo_case(self, tache) -> str:
        liste_tache = self.page.get_by_role("listitem").filter(has_text=tache)
        return liste_tache.get_by_role("checkbox")

    def coche_task(self, tache):
        self.find_todo_case(tache).check()

    def check_count(self):
        return self.page.locator(".todo-count")

    def click_filter(self, nom):
        self.page.get_by_role("link", name=nom).click()

    def clear_completed(self):
        self.page.get_by_role("button", name="Clear completed").click()

    def button_clear_completed(self):
        return self.page.get_by_role("button", name="Clear completed")

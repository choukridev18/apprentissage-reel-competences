from playwright.sync_api import Page, expect
from pages.todo_page import TodoPage


def test_shows_field_todo_on_main_page(page: Page):
    nav = TodoPage(page)
    nav.navigate()
    expect(nav.champs).to_be_visible()


def test_create_todo(page: Page):
    create = TodoPage(page)
    create.navigate()
    create.fill_field_todo_and_submit("acheter du lait")
    expect(create.page.get_by_text("acheter du lait")).to_be_visible()


def test_check_task(page: Page):
    check = TodoPage(page)
    check.navigate()
    check.fill_field_todo_and_submit("acheter du lait")
    check.coche_task("acheter du lait")
    expect(check.find_todo_case("acheter du lait")).to_be_checked()


def test_get_account_after_todo_created(page: Page):
    result = TodoPage(page)
    result.navigate()
    result.fill_field_todo_and_submit("acheter du lait")
    expect(result.check_count()).to_have_text("1 item left")


def test_count_is_zero_after_todo_completed(page: Page):
    count = TodoPage(page)
    count.navigate()
    count.fill_field_todo_and_submit("ma tache")
    count.coche_task("ma tache")
    expect(count.check_count()).to_have_text("0 items left")


def test_completed_filter_hides_active_todo(page: Page):
    completed = TodoPage(page)
    completed.navigate()
    completed.fill_field_todo_and_submit("laver la voiture")
    completed.fill_field_todo_and_submit("acheter du lait")
    completed.coche_task("acheter du lait")
    completed.click_filter("Completed")
    expect(completed.page.get_by_text("laver la voiture")).not_to_be_visible()
    expect(completed.page.get_by_text("acheter du lait")).to_be_visible()


def test_active_filter_hides_active_todo(page: Page):
    active = TodoPage(page)
    active.navigate()
    active.fill_field_todo_and_submit("laver la voiture")
    active.fill_field_todo_and_submit("acheter du lait")
    active.coche_task("acheter du lait")
    active.click_filter("Active")
    expect(active.page.get_by_text("laver la voiture")).to_be_visible()
    expect(active.page.get_by_text("acheter du lait")).not_to_be_visible()


def test_shows_button_clear_completed(page: Page):
    button = TodoPage(page)
    button.navigate()
    button.fill_field_todo_and_submit("laver la voiture")
    button.coche_task("laver la voiture")
    expect(button.button_clear_completed()).to_be_visible()


def test_button_clear_completed_disappear(page: Page):
    button = TodoPage(page)
    button.navigate()
    button.fill_field_todo_and_submit("laver la voiture")
    button.coche_task("laver la voiture")
    button.clear_completed()
    expect(button.button_clear_completed()).not_to_be_visible()

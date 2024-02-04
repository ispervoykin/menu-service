from conftest import client

from src.urls import reverse

menu_id = 1
submenu_id = 1
dish_id = 1


def test_create_menu() -> None:
    global menu_id
    post_json = {
        'title': 'My menu 1',
        'description': 'My menu description 1'
    }
    response = client.post(reverse('menus'), json=post_json)
    response_json = response.json()
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 201
    assert 'id' in response_json
    menu_id = response_json['id']


def test_create_submenu() -> None:
    global submenu_id
    post_json = {
        'title': 'My submenu 1',
        'description': 'My submenu description 1'
    }
    response = client.post(reverse('submenus', kwargs={'menu_id': menu_id}), json=post_json)
    response_json = response.json()
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 201
    assert 'id' in response_json
    submenu_id = response_json['id']


def test_create_first_dish() -> None:
    global dish_id
    post_json = {
        'title': 'My dish 1',
        'description': 'My dish description 1',
        'price': '12.50'
    }
    response = client.post(reverse('dishes', kwargs={'menu_id': menu_id, 'submenu_id': submenu_id}), json=post_json)
    response_json = response.json()
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 201
    assert 'id' in response_json
    dish_id = response_json['id']


def test_create_second_dish() -> None:
    global dish_id
    post_json = {
        'title': 'My dish 2',
        'description': 'My dish description 2',
        'price': '12.50'
    }
    response = client.post(reverse('dishes', kwargs={'menu_id': menu_id, 'submenu_id': submenu_id}), json=post_json)
    response_json = response.json()
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 201
    assert 'id' in response_json
    dish_id = response_json['id']


def test_get_menu_success() -> None:
    response = client.get(reverse('menu', kwargs={'menu_id': menu_id}))
    response_json = response.json()
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 200
    assert 'id' in response_json
    assert 'submenus_count' in response_json
    assert 'dishes_count' in response_json


def test_get_submenu_success() -> None:
    response = client.get(reverse('submenu', kwargs={'menu_id': menu_id, 'submenu_id': submenu_id}))
    response_json = response.json()
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 200
    assert 'id' in response_json
    assert 'dishes_count' in response_json


def test_delete_submenu() -> None:
    response = client.delete(reverse('submenu', kwargs={'menu_id': menu_id, 'submenu_id': submenu_id}))
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.json() is None


def test_get_submenus_empty() -> None:
    response = client.get(reverse('submenus', kwargs={'menu_id': menu_id}))
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 200
    assert response.json() == []


def test_get_dishes_empty() -> None:
    response = client.get(reverse('dishes', kwargs={'menu_id': menu_id, 'submenu_id': submenu_id}))
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 200
    assert response.json() == []


def test_get_menu_success2() -> None:
    response = client.get(reverse('menu', kwargs={'menu_id': menu_id}))
    response_json = response.json()
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 200
    assert 'id' in response_json
    assert 'submenus_count' in response_json
    assert 'dishes_count' in response_json


def test_delete_menu() -> None:
    response = client.delete(reverse('menu', kwargs={'menu_id': menu_id}))
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.json() is None


def test_get_menus_empty() -> None:
    response = client.get(reverse('menus'))
    assert response.headers.get('Content-Type') == 'application/json'
    assert response.status_code == 200
    assert response.json() == []

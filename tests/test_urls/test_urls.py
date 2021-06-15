import pytest

from src.models import Offer, Category

'''admin urls'''
def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200

'''offer urls'''
@pytest.mark.django_db
def test_offers_with_client_get(client):
    response = client.get('/offers/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_offers_with_client_put(basic_offer, client):
    response = client.put(f'/offers/{basic_offer.id}/', data={
        'title': basic_offer.title,
        'description': basic_offer.description,
        'price': round(basic_offer.price, 2),
        'created_at': basic_offer.created_at,
        'category': basic_offer.category.id,
    }, content_type='application/json')
    assert response.data['id'] == basic_offer.id
    assert response.status_code == 200
    assert len(Offer.objects.all()) == 1


@pytest.mark.django_db
def test_offers_with_client_put_incomplete_data(basic_offer, client):
    response = client.put(f'/offers/{basic_offer.id}/', data={
        'title': basic_offer.title,
    }, content_type='application/json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_offer_with_client_get(basic_offer, client):
    response = client.get(f'/offers/{basic_offer.id}/')
    assert response.status_code == 200
    assert response.content.decode() != '{"detail":"Not found."}'

@pytest.mark.django_db
def test_offer_with_client_delete(basic_offer, client):
    response = client.delete(f'/offers/{basic_offer.id}/')
    assert response.status_code == 204


'''category urls'''
@pytest.mark.django_db
def test_category_with_client_get(client):
    response = client.get('/category/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_category_with_client_put(basic_category, client):
    response = client.put(f'/category/{basic_category.id}/', data={
        'name': basic_category.name,
    }, content_type='application/json')
    assert response.data['id'] == basic_category.id
    assert response.data == {'id': basic_category.id, 'name': basic_category.name}
    assert response.status_code == 200
    assert len(Category.objects.all()) == 1


@pytest.mark.django_db
def test_category_with_client_put_incomplete_data(basic_category, client):
    response = client.put(f'/category/{basic_category.id}/', data={},
                          content_type='application/json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_category_with_client_get(basic_category, client):
    response = client.get(f'/category/{basic_category.id}/')
    assert response.status_code == 200
    assert response.data != '{"detail":"Not found."}'


@pytest.mark.django_db
def test_category_with_client_delete(basic_category, client):
    response = client.delete(f'/category/{basic_category.id}/')
    assert response.status_code == 204



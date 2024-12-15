run:
	python3 manage.py runserver

sh:
	python3 manage.py shell

mg:
	python3 manage.py makemigrations

m:
	python3 manage.py migrate

s_user:
	python3 manage.py createsuperuser

dump_category:
	python3 manage.py dumpdata products.ProductCategory > ./fixtures/categories.json

dump_product:
	python3 manage.py dumpdata products.Product > ./fixtures/product.json

load_category:
	python3 manage.py loaddata fixtures/categories.json

load_product:
	python3 manage.py loaddata fixtures/product.json

test:
	python3 manage.py test .

celery:
	celery -A store worker -l INFO
# Project Setup

1. Ensure Pipenv is installed locally: `pip install pipenv`
2. Create or activate a virtual env: `pipenv shell`.
   - Note: remember to select the right python interpreter in the IDE
3. Add Django dependency: `pipenv install django`
   - rest framework: `pipenv install djangorestframework`
4. Initiate a new project: `django-admin startproject config`
5. Remove the top level `config` folder if it has a nested `config` folder inside
6. Create the product app, including the `apps.py`
7. Setup database then run migrations
8. create a designer
   ```bash
   curl -X POST http://localhost:8000/api/designer/ \
   -H "Content-Type: application/json" \
   -d '{
      "name": "BZ"
   }'
   ```
9. create a product

```bash
curl -X POST http://localhost:8000/api/products/ \
-H "Content-Type: application/json" \
-d '{
    "name": "Tom",
    "description": "A high-end smartphone",
    "price": 699.99,
    "designer_id": 1
}'
```

9. Get products `curl -X GET http://localhost:8000/api/products/`

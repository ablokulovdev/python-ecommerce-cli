# python-ecommerce

foydalanuvchilar dastur orqali mahsulotlarni harid qiladi.

# Objects

- User - foydalanuvchilar
- Product - mahsulotlar
- Cart - savatcha
- Cart Item - savatchadagi mahsulotlar
- Order - buyurtma yoki harid
- Order Item - buyurtma yoki hariddagi har bir mahsulot


# Models

- User
    - Fields:
        - id
        - username
        - password
        - first_name
        - last_name
    - Methods:
        - register
        - login
        - logout
        - add cart item into cart
        - delete cart item into cart
        - make order

- Product
    - Fields:
        - id 
        - name
        - category
        - price
        - sale
        - stock
        - description
    - Methods:
        - add product
        - delete product
        - increase product
        - decrease product

- Cart
    - Fields:
        - id
        - user_id

- CartItem
    - Fields:
        - id
        - product_id
        - quantity
        - cart_id

- Order
    - Fields:
        - id
        - user_id
        - total_price

- OrderItem
    - Fields:
        - id
        - order_it
        - product_id
        - quantity
        - 


```
python-ecommerce/

│
├── main.py                  # entry point
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── product.py
│   ├── cart.py
│   ├── order.py
│
├── services/
│   ├── __init__.py
│   ├── auth_service.py      # register / login / logout
│   ├── product_service.py   # product bilan ishlash
│   ├── cart_service.py      # cart + cart item
│   └── order_service.py     # order + order item
│
├── storage/
│   ├── __init__.py
│   └── db.py                # vaqtincha in-memory storage
│
├── cli/
│   ├── __init__.py
│   ├── menu.py
│   └── commands.py
│
└── utils.py                 # helperlar
```
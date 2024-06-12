import streamlit as st

# CSS to inject a colorful header and footer
st.markdown(
    """
    <style>
    .header {
        background: linear-gradient(90deg, rgba(255,0,150,1) 0%, rgba(0,204,255,1) 50%, rgba(0,255,204,1) 100%);
        padding: 20px 0;
        color: white;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .footer {
        background: linear-gradient(90deg, rgba(0,204,255,1) 0%, rgba(255,0,150,1) 50%, rgba(0,255,204,1) 100%);
        padding: 20px 0;
        color: white;
        text-align: center;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .footer a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    .footer-icons img {
        width: 24px;
        margin: 0 10px;
    }
    .main-content {
        padding: 0 20px;
    }
    .navbar {
        background: linear-gradient(90deg, rgba(255,0,150,1) 0%, rgba(0,204,255,1) 50%, rgba(0,255,204,1) 100%);
        overflow: hidden;
    }
    .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
        font-size: 17px;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    @media screen and (max-width: 600px) {
        .navbar a {
            float: none;
            display: block;
            width: 100%;
            text-align: left;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the colorful header
st.markdown('<div class="header">Mobile Accessories E-commerce Store</div>', unsafe_allow_html=True)

# Add some space between header and first product
st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

# Add navbar for "Home", "Products", and "Contact"
st.markdown('<div class="navbar"><a href="#home">Home</a><a href="#products">Products</a><a href="#contact">Contact</a></div>', unsafe_allow_html=True)

# Add dummy text for "Home" section
st.markdown('<div id="home" class="main-content"><h2>Home Section</h2><p>Welcome to our mobile accessories store! We offer a wide range of products to enhance your mobile experience.</p></div>', unsafe_allow_html=True)

# Add dummy text for "Products" section
st.markdown('<div id="products" class="main-content" style="display: none;"><h2>Products Section</h2><p>Check out our latest collection of mobile accessories, including phone cases, screen protectors, and wireless chargers.</p></div>', unsafe_allow_html=True)

# Add dummy text for "Contact" section
st.markdown('<div id="contact" class="main-content" style="display: none;"><h2>Contact Us</h2><p>If you have any questions or inquiries, feel free to contact us:</p><ul><li>Phone: +123-456-7890</li><li>Email: contact@mobileaccessories.com</li><li>Address: 123 Main Street, City, Country</li></ul></div>', unsafe_allow_html=True)

# Add button to show/hide "Products" section
if st.button("Show Products"):
    st.markdown('<script>document.getElementById("products").style.display = "block";</script>', unsafe_allow_html=True)

# Sample product data
products = [
    {"id": 1, "name": "Phone Case", "price": 9.99, "description": "Durable phone case", "image": "phone_case.jpg"},
    {"id": 2, "name": "Screen Protector", "price": 5.99, "description": "Tempered glass screen protector", "image": "screen_protector.jpg"},
    {"id": 3, "name": "Wireless Charger", "price": 19.99, "description": "Fast wireless charger", "image": "wireless_charger.jpg"},
]

# Display products
for product in products:
    st.image(product["image"], use_column_width=True)  # Display the image full width
    st.write(f"**{product['name']}**")
    st.write(f"${product['price']}")
    st.write(product["description"])
    if st.button(f"Add to Cart", key=product["id"]):
        st.session_state["cart"].append(product)
        st.success(f"Added {product['name']} to cart!")

# Display shopping cart
st.sidebar.title("Shopping Cart")
if "cart" not in st.session_state:
    st.session_state["cart"] = []

if st.session_state["cart"]:
    total_price = 0
    for item in st.session_state["cart"]:
        st.sidebar.write(f"{item['name']} - ${item['price']}")
        total_price += item["price"]
    st.sidebar.write(f"**Total: ${total_price:.2f}**")
    if st.sidebar.button("Checkout"):
        st.sidebar.write("Checkout process here")
        st.session_state["cart"] = []
else:
    st.sidebar.write("Your cart is empty")

# HTML for the colorful footer
st.markdown(
    """
    <div class="footer">
        <div class="footer-icons">
            <a href="https://www.facebook.com/"><img src="https://img.icons8.com/fluent/48/000000/facebook-new.png"/></a>
            <a href="https://twitter.com/"><img src="https://img.icons8.com/fluent/48/000000/twitter.png"/></a>
            <a href="https://www.instagram.com/"><img src="https://img.icons8.com/fluent/48/000000/instagram-new.png"/></a>
        </div>
        <div>© 2024 Mobile Accessories E-commerce Store</div>
    </div>
    """,
    unsafe_allow_html=True
)


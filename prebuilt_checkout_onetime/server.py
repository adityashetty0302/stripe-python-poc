import stripe
import os
from flask import Flask, redirect, request


stripe.api_key = "api_key"

app = Flask(__name__, static_url_path="", static_folder=".")

YOUR_DOMAIN = "http://localhost:4242"


@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=[
                "card",
            ],
            line_items=[
                {
                    # TODO: replace this with the `price` of the product you want to sell
                    "price": "price_id",
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=YOUR_DOMAIN + "/success.html",
            cancel_url=YOUR_DOMAIN + "/cancel.html",
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


if __name__ == "__main__":
    app.run(port=4242)
